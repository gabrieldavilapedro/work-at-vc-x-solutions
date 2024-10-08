import pandas as pd
from django.core.management.base import BaseCommand
from core.models import Author
from datetime import datetime


class Command(BaseCommand):
    help = "Import authors from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="The path to the CSV file")
        parser.add_argument(
            "--batch_size",
            type=int,
            default=1000,
            help="The number of records to insert in each batch",
        )

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        batch_size = kwargs["batch_size"]

        count = 0
        for batch in pd.read_csv(file_path, chunksize=batch_size):
            authors = []
            for index, row in batch.iterrows():
                authors.append(Author(name=row["name"]))
            Author.objects.bulk_create(authors)
            hora_atual = datetime.now().strftime("%H:%M:%S")
            count += 1
            self.stdout.write(f"lote {count} inserido {hora_atual}")

        self.stdout.write(self.style.SUCCESS("Successfully imported authors"))
