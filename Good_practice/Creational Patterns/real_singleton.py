class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AppConfig, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, config_file):
        if self._initialized:
            return
        self.config_file = config_file
        self.settings = self.load_config(config_file)
        self._initialized = True

    def load_config(self, config_file):
        # Předstíráme načítání konfigurace z souboru
        return {
            "database": "mysql",
            "host": "localhost",
            "port": 3306
        }

# Použití singletonu
config1 = AppConfig("config.yaml")
print(config1.settings)

config2 = AppConfig("other_config.yaml")
print(config2.settings)

print(config1 is config2)  # True