from ftplib import * #type: ignore

ftp = FTP('ftp.ibiblio.org')

print(ftp.getwelcome())

ftp.quit()