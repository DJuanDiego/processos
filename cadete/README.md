Convertendo vários arquivos de áudio com Bash + FFmpeg
===================

# Dependências:

## Computador com Linux instalado:

Qualquer versão do sistema operacional com o programa/pacote ffmpeg instalado.

## Instalação do FFmpeg (se necessário):

* Debian e derivados, abra um terminal e digite:
```sh
$ sudo apt install ffmpeg
```

* Arch e derivados, abra um terminal e digite:
```sh
$ sudo pacman -S ffmpeg
```

* MacOS, Windows SubSystem for Linux e outras distribuições consulte [https://ffmpeg.org/download.html].


## Arquivos de áudio

Arquivos de áudio a serem convertidos. Todos precisam estar na mesma pasta/diretório.


# Passo a Passo -- Com atalhos para facilitar. ;)

* Abra a pasta/diretório dos arquivos a serem convertidos;

* Copie o endereço da pasta/diretório (Control+L, Control+C);

* Abra um terminal e digite:
```sh
$ cd \[endereço_da_pasta/diretório\] \
# Se não quiser digitar pressione Control+Shift+V ou Shift+Insert para colar o endereço da pasta/diretório que contém os arquivos.
```

* Como exemplo converterei arquivos *.ogg para *.mp3. No terminal digite:
```sh
$ for i in *.ogg; do ffmpeg -i "$i" -f mp3 "${i%.*}.mp3"; done
```

* Se tudo correu bem seus arquivos foram convertidos;

* Para remover os arquivos *.ogg (desnecessários), no terminal:
```sh
$ rm *.ogg
```


# Para saber mais

Existem outras opções de conversão de arquivos utilizando o ffmpeg. Você pode utilizar o site [https://ffmpeg.org/documentation.html] ou usar o manual direto do terminal, ambos em inglês:
```sh
$ man ffmpeg
```
