# CultureX Sprint 3 - Integração de Totem Inteligente
# Gerenciamento de Configuração para Arquitetura Profissional

import os
import logging
from dataclasses import dataclass
from typing import Dict, Any, List

@dataclass
class ConfiguracaoBancoDados:
    """Configuração do banco de dados com validação de segurança"""
    host: str = "localhost"
    porta: int = 5432
    banco_dados: str = "culturex_totem"
    usuario: str = "culturex_user"
    senha: str = "senha_segura"
    caminho_sqlite: str = "data/culturex_integrado.db"
    
    def obter_string_conexao(self, usar_sqlite: bool = True) -> str:
        if usar_sqlite:
            return f"sqlite:///{self.caminho_sqlite}"
        return f"postgresql://{self.usuario}:{self.senha}@{self.host}:{self.porta}/{self.banco_dados}"

@dataclass
class ConfiguracaoSensor:
    """Configuração do sensor ESP32 com validação"""
    ip_esp32: str = "192.168.1.100"
    porta_websocket: int = 8765
    broker_mqtt: str = "localhost"
    porta_mqtt: int = 1883
    validacao_dados_habilitada: bool = True
    temperatura_maxima: float = 50.0
    temperatura_minima: float = -10.0
    umidade_maxima: float = 100.0
    umidade_minima: float = 0.0

@dataclass
class ConfiguracaoML:
    """Configuração de Machine Learning"""
    caminho_modelo: str = "models/"
    metricas_avaliacao: List[str] = None
    tamanho_teste: float = 0.2
    estado_aleatorio: int = 42
    
    def __post_init__(self):
        if self.metricas_avaliacao is None:
            self.metricas_avaliacao = ["precisao", "exatidao", "recall", "f1", "mae", "rmse"]

@dataclass
class ConfiguracaoSeguranca:
    """Configuração de cibersegurança"""
    habilitar_validacao_entrada: bool = True
    habilitar_criptografia_dados: bool = False
    taxa_maxima_requisicoes: int = 100
    ids_sensores_permitidos: List[str] = None
    
    def __post_init__(self):
        if self.ids_sensores_permitidos is None:
            self.ids_sensores_permitidos = ["PRES_001", "TOUCH_001", "PROX_001", "TEMP_001", "HUM_001", "LIGHT_001"]

class ConfiguracaoCultureX:
    """Classe principal de configuração para o Totem Inteligente CultureX"""
    
    def __init__(self):
        self.banco_dados = ConfiguracaoBancoDados()
        self.sensores = ConfiguracaoSensor()
        self.ml = ConfiguracaoML()
        self.seguranca = ConfiguracaoSeguranca()
        self.validar_ambiente()
        self.configurar_logging()
    
    def validar_ambiente(self) -> bool:
        """Validar ambiente do sistema e dependências"""
        diretorios_necessarios = ["data", "models", "logs", "reports"]
        
        for diretorio in diretorios_necessarios:
            os.makedirs(diretorio, exist_ok=True)
        
        return True
    
    def configurar_logging(self):
        """Configurar logging profissional"""
        formato_log = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
        # Configurar logger raiz
        logging.basicConfig(
            level=logging.INFO,
            format=formato_log,
            handlers=[
                logging.FileHandler('logs/sistema_culturex.log'),
                logging.StreamHandler()
            ]
        )

def obter_configuracao():
    """Obter instância de configuração"""
    return ConfiguracaoCultureX()