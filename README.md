# IDP_Captura_Tratamento

Código criado como requisito para a resposta ao exercício final da disciplina de Técnicas Avançadas de Captura e Tratamento de dados. 

O arquivo captura_patentes.py realiza um scraping simples na página https://www.google.com/googlebooks/uspto-patents-grants-text.html, em busca de informações sobre a quantidade de patentes registradas nos Estados Unidos no período entre 1976 e 2015. Como resultado desse scrapping, são salvos um arquivo picle e um arquivo json, cada um deles com um dicionário composto do ano analisado como chave, e pelos links dos arquivos .zip das patentes como valores.

No código, como sugestão do professor, montei mais um dicionário ao final, com o ano como chave e com o tamanho dos arquivos zips correspondentes ao ano como valores. Assim, tem-se um melhor panorama da quantidade de patentes geradas por ano.
