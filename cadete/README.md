Convertendo vários arquivos de áudio com Bash + FFmpeg
===================

# Dependências

## Computador com Linux instalado

Qualquer versão do sistema operacional com o programa/pacote ffmpeg instalado.

## Instalação do FFmpeg (se necessário)

* Debian e derivados:
```sh
$ sudo apt install ffmpeg
```

* Arch e derivados
```sh
$ sudo pacman -S ffmpeg
```

* MacOS e outras distribuições consulte [https://ffmpeg.org/download.html].


## Arquivos de áudio

Arquivos de áudio a serem convertidos.


# Passo a Passo -- Com atalhos para facilitar. ;)

* Abra a pasta dos arquivos a serem convertidos;

* Copie o endereço da pasta (Ctrl+L, Ctrl+C);

* Abra um terminal e digite:

```sh
$ cd \[endereço_da_pasta\] \
# Se não quiser digitar pressione Ctrl+Shift+V ou Shift+Insert para colar o endereço da pasta que contém os arquivos
```

* Como exemplo converterei arquivos *.wav para *.mp3

```sh
$ for i in *.wav; do ffmpeg -i "$i" -f mp3 "${i%}.mp3"; done
```

* Se tudo correu bem seus arquivos foram convertidos;

# Para saber mais

Existem outras opções de conversão de arquivos utilizando o ffmpeg. Você pode utilizar o site [https://ffmpeg.org/documentation.html], em inglês, ou usar o manual direto do terminal:

```sh
$ man ffmpeg
```
