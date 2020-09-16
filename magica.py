arquivo = open('arquivo.txt', 'r')
html = open('hodometro.html', 'w')
for linha in arquivo:
    #html.write(html_str)
    sentence = linha.split('\t')
    hash_imagem = sentence[2].split('?id=')
    html.write('<p>'+sentence[0]+'</p><p>'+sentence[1]+'</p><iframe src="https://drive.google.com/file/d/'+hash_imagem[1]+'/preview" width="640" height="480"></iframe>')
arquivo.close()
html.close()