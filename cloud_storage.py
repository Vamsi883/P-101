import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
       
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BFfTfm-KQo0wMjF9mj6x5J0jKXQGdHF_UQ0xxgheLgIhE_odPLDWVi1fhtI70jyQdU2EZpyCYlgjrwlO5MCgTDrv9gC6GlRZd-C9Y2YwiWpS7xlk27HUcHn6Z5MBt58I8cAuYxw'
    transferData = TransferData(access_token)

    file_from = input("enter file path to transfer to :-")
    file_to = input("enter the full path to dropbox :-")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved!!!")
main()  
