import requests as req

QUERY = 'iphone'
url = 'https://www.olx.com.br/brasil?q=iphone&sf=1'

# ESSA REQUISIÇÃO NÃO DEU CERTO (CóDIGO 403, forbidden), porque não estamos 
# com os COOKIES e os HEADERS adequados para a autorização do site.

# 1- ACESSAR A URL COM O NAVEGADOR (CHROME, FIREFOX)
# 2 - APERTAR F12 E IR PARA A ABA NETWORK
# 3 - RECARREGAR A PÁGINA
# 4 - Botão direito sobre a primeira resuiqição get para COPIAR OS PARÂMETROS (Copy as cURL)
# 5 - IMPORTAR ESSA REQUISIÇÃO NO SOFTWARE POSTMAN

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
	'Referer': 'https://www.olx.com.br/brasil?o=28&q=iphone',
	'Connection': 'keep-alive',
	'Cookie': 'fp_id=778830d8dc25de70467f2d3ac42a094c; sq=ca=11_a&zn=2820&sd=2822&sst=u&st=a&w=5&cg=1120&f=a; _hjid=ebe116b4-d13e-4538-8ea8-6fbbb2d5fb1d; r_id=7942f910-2867-4f65-82b6-92e2061e7015; TestAB_Groups=adv-tails_enabled.advRefreshSlotScroll_A.autos-native-vas_a.banner-corona-web_show.banner-lgpd-web_show.cars-adview-financiable_enabled.cdrelrank-guanabara_control.help-center-new-pre-chat_A.helpcenter-chat_A.helpcenter-new-categories_A.helpcenter-selfservice-pending-publishing_A.hug-help-center-new-pre-chat_control.imo-estande-virtual_show.listingadvertisement_selobv.mes-1860-chatlist_50.mes-corona-virus-tip_enabled.myads-new-expired_A.myads-new-pendingpay_A.myads-new-pendingpublish_A.myads-new-published_A.osp-new-front-web_new-front.pp-myplan-header-button_show.pp-product-visual-highlight-web_super-vitrine-active.rec-adv-imo-lancamentos-interleaving_single-slot.removalAdOnboard_A.transactions-signup_enabled.upr-chat-adview-profilelink_A.upr-chat-listing-profilelink_A.uprNewProMiniProfile_enabled.uprNewProProfile_enabled.uprViewUserProfileVerifiedIcon_enabled.vas-autos-chat_4.vasimo-btn-simulator_enabled.vx-myads-insertion_modal.vx-tag-listing_active.vx-videos-on-adview-gallery_second-position.wallet-chatbot_control.webpush-offer-web_show; session_id=778830d8dc25de70467f2d3ac42a094c; nl_id=3bf88f30-ed4c-409e-a89c-e842aaa638d8; _gcl_au=1.1.338589502.1602808457; __cfduid=d3617ead6a5b80f27920468daad3e0c651602808457; __cf_bm=8ff2c2ec7502c9cece62323602de06981b1e8367-1602808541-1800-AerKZFSQ1c9jbrE8G+3pJU8GHpS5UfUFx6E/Nf9SquO1QNgm2t0CWz/y6u7vZ1RwhTz2R9UHW18jBuczipPJc9Ocz3Bxu1pRbkACsp01GlzclNAewQ31bdukgUZQFocxvQ==; _ga=GA1.3.1699249505.1602808462; _gid=GA1.3.45986886.1602808462; l_id=ac7b4e5b-ef46-49d4-9239-815a13dd0f95; s_id=90540686-ba67-4203-b507-4d5092951bc32020-10-16T00:34:26.076Z; tt_c_vmt=1602808466; tt_c_c=search; tt_c_s=search; tt_c_m=search; _ttuu.s=1602809128730; tt.u=7C0B000AB4840A5D0B02F0110239594E; _hjIncludedInSessionSample=0; _hjTLDTest=1; _hjAbsoluteSessionInProgress=1; tt.nprf=; _ttdmp=E:1|X:4|G:1|U:67|LS:|CA:CA17983,CA18724,CA18729; las=801197738; r_id=7942f910-2867-4f65-82b6-92e2061e7015; TestAB_Groups=adv-tails_enabled.advRefreshSlotScroll_A.autos-native-vas_a.banner-corona-web_show.banner-lgpd-web_show.cars-adview-financiable_enabled.cdrelrank-guanabara_control.help-center-new-pre-chat_A.helpcenter-chat_A.helpcenter-new-categories_A.helpcenter-selfservice-pending-publishing_A.hug-help-center-new-pre-chat_control.imo-estande-virtual_show.listingadvertisement_selobv.mes-1860-chatlist_50.mes-corona-virus-tip_enabled.myads-new-expired_A.myads-new-pendingpay_A.myads-new-pendingpublish_A.myads-new-published_A.osp-new-front-web_new-front.pp-myplan-header-button_show.pp-product-visual-highlight-web_super-vitrine-active.rec-adv-imo-lancamentos-interleaving_single-slot.removalAdOnboard_A.transactions-signup_enabled.upr-chat-adview-profilelink_A.upr-chat-listing-profilelink_A.uprNewProMiniProfile_enabled.uprNewProProfile_enabled.uprViewUserProfileVerifiedIcon_enabled.vas-autos-chat_4.vasimo-btn-simulator_enabled.vx-myads-insertion_modal.vx-tag-listing_active.vx-videos-on-adview-gallery_second-position.wallet-chatbot_control.webpush-offer-web_show',
	'Upgrade-Insecure-Requests': '1',
	'Cache-Control': 'max-age=0'
}

r = req.get(url,headers=headers)
print(r.status_code)

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.content, 'lxml')
anuncios = soup.find('ul',{'id':'ad-list'})

print(r.content)
