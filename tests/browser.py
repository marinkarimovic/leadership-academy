from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
server=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=__import__('os').environ.get('CHROMIUM_PATH','/usr/bin/chromium'),args=['--no-sandbox']);page=b.new_page(viewport={'width':390,'height':844});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(f'http://127.0.0.1:{server.server_port}/');page.get_by_role('checkbox').first.check();page.reload();assert page.get_by_role('checkbox').first.is_checked();page.get_by_role('button',name='Zeit',exact=True).click();page.get_by_role('button',name='Timer starten').click();page.wait_for_timeout(1100);page.reload();page.get_by_role('button',name='Zeit',exact=True).click();page.get_by_role('button',name='Pause').click();page.get_by_role('button',name='Beenden & speichern').click();assert page.get_by_text('Lernhistorie').is_visible();page.get_by_role('button',name='Journal',exact=True).click();page.locator('textarea').first.fill('Testreflexion');page.reload();page.get_by_role('button',name='Journal',exact=True).click();assert page.locator('textarea').first.input_value()=='Testreflexion';
 for name in ['Plan','Skills','Coach','Karriere','Heute']:
  page.get_by_role('button',name=name,exact=True).click()
 assert not errors,errors
 b.close()
print('Browser smoke test PASS')
