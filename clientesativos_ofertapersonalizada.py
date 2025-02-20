import undetected_chromedriver as uc
import time

# Inicializa o WebDriver no modo "stealth"
driver = uc.Chrome()

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com/")
input("Escaneie o QR Code e pressione Enter para continuar...")

# Lista de números
numeros = ["+5511973275740", "+5511985226528", "+5511996458374", "+5511957544620", "+5511965149037", "+5511954990078", "+5511947435307", "+5511963460014", "+5511982568105", "+5511967133414", "+551198467165", "+551198432781", "+5511982299919", "+5517981718808", "+551198467165", "+551194007843", "+5511954943129", "+5511982578116", "+5511930378816", "+551198482194", "+551177963399", "+5511954399647", "+551198432781", "+5511999168105", "+551151638242", "+5511949032459", "+5511998921272", "+5511952168301", "+5511918677347", "+5511968749300", "+551196874930", "+5511948104960", "+5511993748526", "+5511949332280", "+5511966649676", "+5511985139645", "+551194101100", "+5511980154764", "+5511937271465", "+5511985270442", "+5511948182887", "+5511977781000", "+551198528428", "+5511951203103", "+5511997192747", "+5511955950386", "+551199766045", "+5511940770449", "+5511947855876", "+5511998498918", "+5511986230451", "+5511951359808", "+5511957899215", "+5511963467391", "+5511970331577", "+551698825423", "+5511962864645", "+5511974216239", "+5511992442569", "+5511994977456", "+5511967171237", "+5511912183249", "+551194781021 ", "+5511948879185", "+5511954325701", "+5511988098864", "+5511964128259", "+5511964341691", "+5511984977995", "+5511984984563", "+5511996816698", "+551194814359", "+5511982169515", "+5511983012683", "+5511977351847", "+5511984814129", "+5511977351847", "+5511952428891", "+5511995882063", "+5511968117857", "+5511941504144", "+5511984518065", "+5511962781248", "+5511954401028", "+5511994976462", "+5511964355596", "+5511991344387", "+5511960366510", "+5511963632461", "+5511952832698", "+5511978605609", "+5511978210990", "+5511977710459", "+5511982956074", "+5511960481834", "+5511982043542", "+5511952428001", "+5511954635721", "+5524998666478", "+5511954247990", "+557599993834", "+5511949953778", "+5511941610178", "+5511949350676", "+5511952386623", "+5511953873539", "+5511977293148", "+5575999850841", "+5511993283979", "+5511982457324", "+5511914035020", "+5511985139645", "+5511989125577", "+5511992244705", "+5511914032772", "+5511934107977", "+5511959429896", "+553899666464", "+5538998674067", "+5511947487136", "+5511934431888", "+5511986229323", "+5511992858784", "+5511993644141", "+5511964607041", "+5511970130013", "+5511980205770", "+5511930126422", "+5511961742354", "+5511987274155", "+5511933504951", "+5511994328525", "+559180934034", "+5511949826773", "+5511954441940", "+5511953501676", "+5511961577640", "+5511983839383", "+5511997410470", "+5511994472885", "+5511953373761", "+551194814359", "+551195883997", "+551195883997", "+5511953041205", "+5511977619288", "+5511987052372", "+5511985554693", "+551195883997 ", "+5511953327611", "+551195883997", "+551195883997", "+551195883997", "+5511961240049", "+5511947763466", "+5511995218900", "+5511974027419", "+5511967556383", "+5511984310624", "+5511963165481", "+5511973439899", "+5511985631383", "+5511981995091", "+5511911954036", "+5511976853400", "+5511978050779", "+5582981683762", "+5511965442316", "+5511973396502", "+5511983880356", "+5511982413210", "+5511954329471", "+5511977180736", "+5511911734100", "+5511991071023", "+5511941854507", "+5511913058319", "+551195377659 ", "+5511979723901", "+5511970193330", "+5511957457814", "+5511977261325", "+5511963699585", "+5511913146353", "+5511987721842", "+5511983018047", "+5511943224646", "+5519996592568", "+5511958697037", "+5511999250357", "+5511992308496", "+5511966820087", "+5511947049103", "+5511977366836", "+5511951756899", "+5511992308496", "+5511946721570", "+5511995057443", "+5511984660417", "+5511978275186", "+5511982495733", "+5511947470798", "+5511958920706", "+5511985196744", "+5511930697268", "+5511987905387", "+5511978050779", "+5511983113838", "+5511941768215", "+5511945622167", "+5511964216387", "+5511977830421", "+5511952033364", "+5511985400640", "+5511930786854", "+5511978160195", "+5511970434517", "+5511998390053", "+5511944492639", "+5511964511102", "+5511985643423", "+5511986104305", "+5511959344833", "+5511940841382", "+5511987237663", "+5511952698191", "+5511979860893", "+5511913371935", "+5511985454603", "+5511982568432", "+5511948675821", "+5575991188088", "+5511960319142", "+5511952027096", "+5511950301724", "+5511982508936", "+5511958726286", "+5511962818147", "+5511977502131", "+5511982871211", "+5511987192851", "+5511999999999", "+5511999999987", "+5511963698055", "+5511964909930"]
mensagem = "✨💅 OFERTA PERSONALIZADA 💖 💅 PACOTE Manicure + Pedicure 👣 🤩 LEIA!!!🔥"

# Enviar mensagens
for numero in numeros:
    url = f"https://web.whatsapp.com/send?phone=55{numero}&text={mensagem}"
    driver.get(url)
    time.sleep(10)

    try:
        send_button = driver.find_element("xpath", '//span[@data-icon="send"]')
        send_button.click()
        print(f"Mensagem enviada para {numero}")
    except Exception as e:
        print(f"Erro ao enviar para {numero}: {e}")

    time.sleep(5)

print("Mensagens enviadas com sucesso!")
driver.quit()
