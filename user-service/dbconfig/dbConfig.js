require('dotenv').config();
const { Pool, Client } = require('pg');
const connectionString = process.env.DB_URL;
let tries = 5;

const pool = new Pool({
    connectionString: connectionString,
});

while (tries > 0) {
    try {
        pool.query("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'", (err, res) => {
            if (err)
                console.log(err);
            else {
                if (!res.rowCount) {
                    console.log("Database not found");
                    console.log("Creating");
                    
                    pool.query(`
                      CREATE TABLE PROFESSOR (
                        matricula int,
                        email varchar(100),
                        nome varchar(30),
                        sobrenome varchar(30),
                        admnistrador bool,
                        senha varchar(1000),

                      CONSTRAINT PROFESSOR_PK PRIMARY KEY(matricula)
                    );

                    CREATE TABLE DISCIPLINA (
                      id SERIAL,
                      nome varchar(100),
                      professor_id int,
                      descricao varchar(10000),

                      CONSTRAINT DISCIPLINA_PK PRIMARY KEY (id),

                      CONSTRAINT DISCIPLINA_PROFESSOR_FK FOREIGN KEY (professor_id)
                          REFERENCES PROFESSOR (matricula)
                    );

                    CREATE TABLE AGENTE_EXTERNO (
                      id SERIAL,
                      email varchar(100),
                      nome_comum varchar(100),
                      descricao varchar(1000),
                      senha varchar(1000),

                      CONSTRAINT AGENTE_EXTERNO_PK PRIMARY KEY (id)
                    );

                    CREATE TABLE PROJETO (
                      id SERIAL,
                      concluido bool,
                      aprovado bool,
                      descricao varchar(1000),
                      agente_externo int,
                      disciplina_aloc int,

                      CONSTRAINT PROJETO_PK PRIMARY KEY (id),

                      CONSTRAINT PROJETO_AGENTE_EXTERNO_FK FOREIGN KEY (agente_externo)
                          REFERENCES AGENTE_EXTERNO (id),
                      CONSTRAINT PROJETO_DISCIPLINA_FK FOREIGN KEY (disciplina_aloc)
                          REFERENCES DISCIPLINA (id)
                    );

                    CREATE TABLE equipe (
                      id SERIAL,
                      nome varchar(20),
                      disciplina_id int,
                      projeto_id int,

                      CONSTRAINT equipe_PK PRIMARY KEY (id),
                      
                      CONSTRAINT equipe_DISCIPLINA_FK FOREIGN KEY (disciplina_id)
                          REFERENCES DISCIPLINA (id),
                      CONSTRAINT equipe_PROJETO_FK FOREIGN KEY (projeto_id)
                          REFERENCES PROJETO(id)

                    );

                    CREATE TABLE ALUNO (
                      matricula int,
                      email varchar(100),
                      nome varchar(30),
                      sobrenome varchar(30),
                      equipe_id int,
                      senha varchar(1000),

                      CONSTRAINT ALUNO_PK PRIMARY KEY(matricula),

                      CONSTRAINT ALUNO_equipe_FK FOREIGN KEY(equipe_id)
                          REFERENCES equipe(id)
                    );

                    CREATE TABLE cursa (
                      aluno_id int,
                      disciplina_id int,

                      CONSTRAINT cursa_ALUNO_FK FOREIGN KEY (aluno_id)
                          REFERENCES ALUNO(matricula),
                      CONSTRAINT cursa_DISCIPLINA_FK FOREIGN KEY (disciplina_id)
                          REFERENCES DISCIPLINA(id)
                    );
                    `, (err, res) => {
                        if (err) {
                            console.log("Failed creating Database");
                            console.log(err);
                        } else {
                            console.log('Database \x1b[32mOK\x1b[0m');
                        }
                    });
                }

                else if (res.rowCount != 7)
                    throw '\x1b[33mFaulty database in project\n\x1b[33mDelete dbdata and start project again';

                else
                    console.log('Database \x1b[32mOK\x1b[0m');
            }
        });
        break;
    } catch (err) {
        console.log(err);
        tries--;
        continue;
    }
}
module.exports = {
    query: (text, params, callback) => {
        return pool.query(text, params, callback);
    },
}
