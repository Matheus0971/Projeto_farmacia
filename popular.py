from datetime import datetime
import random
from model import SessionLocal, Farmaceutico, Cliente, Venda

def popular_banco():
    session = SessionLocal()

    try:
        # 1. Inserir Farmacêuticos
        farmaceuticos = [
            Farmaceutico(nome="Ana Silva", crf="CRF/SP 12345"),
            Farmaceutico(nome="Carlos Oliveira", crf="CRF/SP 67890"),
            Farmaceutico(nome="Mariana Costa", crf="CRF/RJ 11223"),
        ]
        session.add_all(farmaceuticos)
        session.commit()

        # 2. Inserir Clientes
        clientes = [
            Cliente(nome="João Pedro", cpf="111.222.333-01"),
            Cliente(nome="Maria Souza", cpf="222.333.444-02"),
            Cliente(nome="Lucas Ferreira", cpf="333.444.555-03"),
            Cliente(nome="Fernanda Lima", cpf="444.555.666-04"),
            Cliente(nome="Beatriz Rocha", cpf="555.666.777-05"),
        ]
        session.add_all(clientes)
        session.commit()

        # 3. Inserir pelo menos 20 Vendas relacionando Farmacêuticos e Clientes
        vendas = []
        for i in range(20):
            f_escolhido = random.choice(farmaceuticos)
            c_escolhido = random.choice(clientes)
            valor = round(random.uniform(15.0, 350.0), 2)

            venda = Venda(
                valor_total=valor,
                farmaceutico_id=f_escolhido.id,
                cliente_id=c_escolhido.id,
                data_venda=datetime.now()
            )
            vendas.append(venda)

        session.add_all(vendas)
        session.commit()

        print(f"Banco populado com sucesso! {len(vendas)} vendas cadastradas.")

    except Exception as e:
        session.rollback()
        print(f"Erro ao popular banco: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    popular_banco()