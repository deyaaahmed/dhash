a
    \�`%4  �                   @   s*  d Z ddlT ddlmZ ddlZzddlZddlZddlZW n eyX   e�d� Y n0 ddlm	Z	m
Z
 ddlmZ ddlZdZd	Zd
ZdZdZdZdZdZdZed� dZdd� Zdd� Zdd� ZdZdZdZdd� Z dZ!dd� Z"ee e e e e! e# e$ e% Z&d d!� Z'e'�  d"d#� Z(e(�  dS )$z^
Who is '7azabet' ?
"7AZABET" is an Ethical Programmer not a hacker, Just a poor programmer .
�    )�*)�getpassNz5pip3 install progressbar readline tqdm alive-progress)�	alive_bar�bouncing_spinner_factory)�sleep�Ez[1;30m�[1;31mz[1;32mz[1;33mz[1;35mz[1;36m�[1;37mzChecking new version...�Kc                   C   s   t �d� d S )N�clear)�os�system� r   r   �d/decrypter.pyr   0   s    r   c                   C   s   t d� td� d S )NzWait..皙�����?)�print�sr   r   r   r   �wait4   s    r   c                   C   s   t d� d S )N� )r   r   r   r   r   �space9   s    r   �o� �lc               
   C   s�   zZt d�} td� | �� dks*| �� dkr2t�  n&| dkrJtd� t�  ntd� t�  W n2 ty� } ztd|� �� W Y d }~n
d }~0 0 d S )	Nz7[1;34mDo you wanna decrypt another hash (y/n): [1;33mr   Zyes�yr   z!Specify an option "yes" or "no" ?z[1;36mExiting, Goodbye :)z[0;91mERROR!
)�inputr   �lower�hash_decrypter�again�exit�	Exception)�aZerr   r   r   r   D   s    
r   �rc                  C   sb   t t� tdddd�} td| d��,}td�D ]}td� |�  q,W d   � n1 sT0    Y  d S )Nu   🤖�   F)Zhiding�d   )�spinnerg���Q��?)r   �Wr   r   �ranger   )r$   Zbar�ir   r   r   �probarW   s    r(   c                  C   s�   t t� � t�  t�d� t�  z$ttd t �a	t
td t �aW n ty^   td� Y n0 d} t�  t	| kr�ttkr�td� t td � nt td � t�  d S )	Nzcat banner/login_banner.txtz
USERNAME: z
PASSWORD: z)

[!] CTRL+C detected, program exiting .
Z7AZABETr   z
[+] Done Successfully ^__^ z
[!] NOT FOUND)r   �Rr   r   r   r   r   r%   r   �usernamer   �password�KeyboardInterruptr   r(   �pr   �G)�userr   r   r   �loginc   s     

r0   c            	   
   C   s  dd l } dd l}td� t�  tdt� d�� td� dd� }t�d� t�d	� t�	|� z t
d
t �at
td t �aW n ty�   t�  Y n0 tdkr�dag d�}tt�|vr�tdt� dt� dt� dt� d�	� td� dt� d�D ]"}td� |j�|� |j��  q�td� �z�ttdd����}|D �]N}|�� }tt�dk�r�| �|�� ��� }|tk�rBtd|� d�� td� t�   �q��n�tt�t| �d�� ��� �k�r�| �|�� ��� }d}|tk�rBtd|� d|� d�� td� t�   �q��nDtt�t| �d�� ��� �k�rl| �|�� ��� }d }|tk�rBtd|� d|� d�� td� t�   �q��n�tt�t| �d�� ��� �k�r�| �|�� ��� }d!}|tk�rBtd|� d|� d�� t�  td�  �q��nhtt�t| �d�� ��� �k�rH| �|�� ��� }d"}|tk�rBtd|� d|� d�� t�  td�  �q��n�tt�t| � d�� ��� �k�r�| � |�� ��� }d#}|tk�rBtd|� d|� d�� t�  td�  �q��n�tt�t| �!d�� ��� �k�r$| �!|�� ��� }d$}|tk�rBtd|� d|� d�� t�  td�  �q��ntt�t| �"d�� ��� �k�r�| �"|�� ��� }d%}|tk�rBtd|� d|� d�� t�  td�  �q��n�tt�t| �#d�� ��� �k�r | �#|�� ��� }d&}|tk�rBtd|� d|� d�� t�  td�  �q��nBtt�t| �$d�� ��� �k�rl| �$|�� ��� }d'}|tk�rBtd|� d|� d�� t�  td�  �q�n�tt�t| �%d�� ��� �k�r�| �%|�� ��� }d(}|tk�rBtd|� d|� d�� t�  td�  �q�njtt�t| �&d�� ��� �k�rB| �&|�� ��� }d)}|tk�rBtd|� d|� d�� t�  td�  �q�tt�t| �"d�� ��� �k�r�| �"|�� ��� }d%}|tk�r~td|� d|� d�� t�  td�  �q�n�tt�t| �d�� ��� �k�r| �|�� ��� }d}|tk�r~td|� d|� d�� t�  td�  �q�ndtt�t| �d�� ��� �k�r0| �|�� ��� }d }|tk�r0td|� d|� d�� t�  td� �q0td*t� d+t� d,�� t�  W d   � n1 �s�0    Y  W n@ t'�y�   td-� Y n& t�y    t(�  ttd. � Y n0 d S )/Nr   r	   uI   [1;37m             ==>[1;31m ^_^ أهلاً بكَ فى عالمى ^_^ z[<==


[1;37mGive me an encrypted word or hash and I will decrypt it
Happy Cracking ^__^ 

g�������?c                 S   s   t � | d �d g | S )Nr   )�glob)�text�stater   r   r   �complete�   s    z hash_decrypter.<locals>.completez 	
;ztab: completezEnter the hashed word: zGEnter the name of wordlist or press Enter to use the default wordlist: r   zdb.txt)�    �(   �8   �@   �`   r7   �   �
�[�!z] zYour Input Is NOT A HashzCracking...
g�������?�   r!   )�moder5   z0[1;37m[[1;32m+[1;37m] Password found: [1;33mz2
[1;37m[[1;32m+[1;37m] Type of hash: [1;33mmd5�test�blake2bz/
[1;37m[[1;32m+[1;37m] Type of hash: [1;33mr   �blake2s�sha1�sha224�sha256�sha384�sha512�sha3_224�sha3_256�sha3_384�sha3_512z"[[1;31m![0;37m] Sorry,But your (z/) is not match any word in the specified file (�)z9[1;37m[[1;31m![1;37m] The specified file is not existszExit :())�hashlib�sysr   Zbannerr%   r   �readline�set_completer_delims�parse_and_bind�set_completerr   r.   Z
hashd_word�filer,   r   �lenr)   �C�stdout�write�flush�open�stripZmd5�encodeZ	hexdigestr   rA   rB   rC   rD   rE   rF   rG   rH   rI   rJ   rK   �FileNotFoundErrorr   )	rM   rN   r4   Zhashlengths�c�f�lineZhashd_word_in_fileZ	type_hashr   r   r   r   �   sv   
�


"


 

�

 

�

 

�

 

�

 

�

 

�

 

�

 

�

 

�
 

�
 

�
 

�
 

�
 

�

�
*r   ))�__doc__Zmymoduler   r   ZprogressbarrO   Zalive_progress�ModuleNotFoundErrorr   r   r   �timer   r   r1   ZfcZblackr)   r.   �Y�B�PrU   r%   r   Zfocr   r   r   ZficZtcZscr   Zsicr(   ZsecZeicZncr-   r0   r   r   r   r   r   �<module>   sL   	$ Q