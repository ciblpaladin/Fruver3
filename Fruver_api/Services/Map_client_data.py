
class Map_data:
    @staticmethod
    def data_to_sp(data_client, delete = ""):

        request_form = dict(data_client.data)

        delete_items = []
        if delete != "":
            for key, value in request_form.items():
                if delete in key:
                    delete_items.append(key)
            for key in delete_items:
                del request_form[key]             
        data = []
        for key ,values in request_form.items():
            for off_list in values: 
                data.append(off_list)  
        return data
    
    def data_build_sp(sp_name ,data_client):
        params_build = ""
        for key, values in data_client.data.items():

            params_build += f"{values},"
            
        sp_build = f"{sp_name}({params_build})"

        if sp_build.endswith(",)"):
            sp_building = sp_build[:-2]
            sp_building += ")"

            return sp_building
     
     