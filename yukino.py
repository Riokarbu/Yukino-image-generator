#https://github.com/Riokarbu
from bing_image_downloader import downloader

def main():
    print("""\                                                                                           
                                                                                          
                                                                                          
                                                 .:===-.                                  
                                  .:-==++++++++++**+-:.:*.                                
                               :=++++++++++++*****+**+++*+:.                              
                            .-+++++++++++++*%%#*++****+++++++-                            
                           -++++++++++++++#%*++++++++++++*#*+++=:                         
                         .+++++++++++++++*#++++++++++++++++*#++++=                        
                        -++++++++++++++++*++++++++++++++++++*#++++=                       
                       :++++++++++++++++*++++++++++++++++++++**+++=:                      
                       ======++++++++++*+++++++++++++*++++++++*====+                      
                      .+++++++++++*++++*+++**+++++++++#++*++++*+++++-                     
                      -++++++++++*+++++#++*+*++*++++++#*++++++*++++++                     
                      =++++++++++#++++**++#+=++*++++++*#++=+++#*+++++-                    
                      =*+++++++++#++++*+++#+-+++#*++++*%*+==*+##*+++#*-                   
                      =*+++*+++++#*++++=++=+.:+**#++++*%**=:=+++*+*++-++:                 
                      -*+*+**++++*#+*++.=+.=..-++*-+++#%**.-+#*=*+*++    .                
                      .*+*+*#+++++#*#+*+**%%%%#+*+-.=+#%*#%%=- :#+%*+-                    
                       ++*+*#++++++%###+ .###*=- -=.:*%#=*##*: .+##%*+.                   
                       -+*+*%++++==#%#*=  #=+=+: ....*--.=::-  :**:%+=+.                  
                       :+***%++++=-*%#*=:......  ..............:+= #.  :                  
                       -+*#+%*+++-:+%#+.::.... ...............:.+:.-                      
                       =+#%+%*++=:-+##+.:::.....................+..                       
                       ++%%*#*++*=:+*#+........................:+                         
                      =+##%##*+#%%%#+*+ ............::........=+-                         
                     :+**####**###%%**+::.........---=:....:=*#+:                         
                     ++-*#%###%%###=+++----::...........:=*%%##*:                         
                    =+: +###*#####+:=++----------::---+#%###%#*+-                         
                   .+-  +##*#####*::-+=------:::-::.#%%#%%%#%%++=                         
                   :+  :+%%%%%-+#+::-+- ..::....:-- :=###%%%%%+++                         
                   --  +*%%##* +##+:-+-.     ::..:: -+:+####%%**+-                        
                   :: -*#####+ *###=-+::    :. .. .:.**-:*######*+.                       
                   =**#######- #####*= ..  :.   :..--*##+.-*####*+=                       
                 :*##########..#####*+   .-=++*##*##****:-*######==-                      
                 *########### .++****#*:::*******:+*=*#+=+*######+ *                      
                :############--:::: -=#*. =++-+*-.:*++##*+.-#####* ==                     
                -++++++++++++++++*-.=++++    .++.. +++++++.:+++*++ :+                     
                                                                                          """)

    print("YUKINO AUTO IMAGE GENERATOR\nGITHUB: github.com/Riokarbu\n")

    while True:
        # Meminta input dari pengguna untuk menentukan jenis gambar yang akan diunduh
        response = input("Select one [y] for sfw no r18 [n] for nsfw +18 (type 'exit' to quit): ")

        if response.lower() == 'exit':
            print("Goodbye!")
            break

        # Memastikan input yang diberikan adalah y atau n
        if response.lower() not in ['y', 'n']:
            print("Invalid input. Please enter 'y' for sfw or 'n' for nsfw.")
            continue

        # Meminta jumlah gambar yang ingin diunduh dari pengguna
        jumlah = int(input("Enter the number of images you want to download: "))

        # Menentukan jenis gambar berdasarkan input pengguna
        if response.lower() == 'y':
            download_query = 'yukino yukinoshita'
            output_dir = 'sfw'
            adult_filter_off = True
        else:
            download_query = 'yukino yukinoshita nude'
            output_dir = 'nsfw'
            adult_filter_off = False

        # Mengunduh gambar sesuai dengan jenis yang dipilih
        result = downloader.download(download_query, limit=jumlah, output_dir=output_dir, adult_filter_off=adult_filter_off, timeout=60)

        if result == 1:
            print("Images downloaded successfully!")
        else:
            print("Failed to download images.")

if __name__ == "__main__":
    main()