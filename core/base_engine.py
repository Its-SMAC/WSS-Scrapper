from abc import ABC, abstractmethod


class BaseEngine(ABC):
    def __init__(self):
        self.data = []
        self.page = None

    @abstractmethod
    def fetch(self, url: str):
        """Lógica para abrir o browser e navegar até ao URL."""
        pass

    @abstractmethod
    def parse(self):
        """Lógica específica de seletores CSS para extrair dados."""
        pass

    def save(self, filename: str):
        """Lógica comum para salvar em JSON/CSV (esta pode ser genérica na base)."""
        print(f"A guardar {len(self.data)} produtos em {filename}...")
        # Aqui fazes o dump do self.data
