# Entidades
class Tarefa:
    def __init__(self, id, titulo, descricao, concluida, prioridade, data_de_criacao):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida
        self.prioridade = prioridade
        self.data_de_criacao = data_de_criacao


# Objeto de Valor para Data de Criação
class DataDeCriacao:
    def __init__(self, ano, mes, dia):
        self.ano = ano
        self.mes = mes
        self.dia = dia

    #def __eq__(self, other):
    #    if not isinstance(other, DataDeCriacao):
    #        return False
    #    return self.ano == other.ano and self.mes == other.mes and self.dia == other.dia

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

    #def __repr__(self):
    #    return f"DataDeCriacao({self.ano}, {self.mes}, {self.dia})"

# Repositório (simulado)
class RepositorioTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        return self.tarefas

# Serviços de Aplicação
class ServicoTarefas:
    def __init__(self, repositorio_tarefas):
        self.repositorio_tarefas = repositorio_tarefas

    def criar_tarefa(self, titulo, descricao, prioridade, data_de_criacao):
        nova_tarefa = Tarefa(len(self.repositorio_tarefas.listar_tarefas()) + 1, titulo, descricao, False, prioridade, data_de_criacao)
        self.repositorio_tarefas.adicionar_tarefa(nova_tarefa)
        return nova_tarefa

    def listar_tarefas(self):
        return self.repositorio_tarefas.listar_tarefas()

# Camada de Apresentação (View)
class TarefasView:
    def mostrar_tarefas(self, tarefas):
        print("Tarefas:")
        for tarefa in tarefas:
            print(f"{tarefa.titulo} - {'Concluída' if tarefa.concluida else 'Pendente'} - Prioridade: {tarefa.prioridade} - Criada em: {tarefa.data_de_criacao}")

# Camada de Apresentação (Controller)
class TarefasController:
    def __init__(self, servico_tarefas, view):
        self.servico_tarefas = servico_tarefas
        self.view = view

    def listar_tarefas(self):
        tarefas = self.servico_tarefas.listar_tarefas()
        self.view.mostrar_tarefas(tarefas)

    def criar_tarefa(self, titulo, descricao, prioridade, data_de_criacao):
        nova_tarefa = self.servico_tarefas.criar_tarefa(titulo, descricao, prioridade, data_de_criacao)
        print(f"Tarefa criada: {nova_tarefa.titulo}")

if __name__ == "__main__":
    repositorio = RepositorioTarefas()
    servico_tarefas = ServicoTarefas(repositorio)
    view = TarefasView()
    controller = TarefasController(servico_tarefas, view)

    # Executar ações do sistema
    controller.criar_tarefa("Comprar leite", "Ir à mercearia", "Alta", DataDeCriacao(2023, 9, 12))
    controller.criar_tarefa("Estudar Python", "Capítulo 5", "Baixa", DataDeCriacao(2023, 9, 13))

    controller.listar_tarefas()

