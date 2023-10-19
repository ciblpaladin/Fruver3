
class Map_data:
    @staticmethod
    def data_to_sp(data_client):

        data = []
    
        for key ,values in data_client.data.items():
            data.append(values)

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
     