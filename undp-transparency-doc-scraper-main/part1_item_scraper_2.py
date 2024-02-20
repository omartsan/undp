from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

def get_files(file_url):
    try:
        site_url = "https://undp.sharepoint.com/"
        credentials = UserCredential('omar.santoyo@undp.org', 'XXXXXX')


        ctx = ClientContext(site_url).with_credentials(credentials)
        
        # file_url is the sharepoint url from which you need the list of files
       # file_url = 'https://undp.sharepoint.com/sites/Docs-Project/Shared%20Documents'

        list_source = ctx.web.get_folder_by_server_relative_url(file_url)

        files = list_source.files
        ctx.load(files)
        ctx.execute_query()

        return files

    except Exception as e:
        print(e)

get_files('https://undp.sharepoint.com/sites/Docs-Project/Shared%20Documents')