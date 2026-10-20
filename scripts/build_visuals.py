"""Generate editable diagram exports and deliberately schematic UX mockups."""
from pathlib import Path
import json, math, html
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def font(n=23,b=False): return ImageFont.truetype(BOLD if b else FONT,n)
def diagram(name,title,nodes,edges,mermaid):
 specpath=ROOT/f'diagrams/src/{name}.json'
 if specpath.exists():
  spec=json.loads(specpath.read_text());title,nodes,edges=spec['title'],spec['nodes'],spec['edges']
 else:
  spec={'title':title,'nodes':nodes,'edges':edges};specpath.write_text(json.dumps(spec,ensure_ascii=False,indent=2))
 (ROOT/f'diagrams/src/{name}.mmd').write_text(mermaid+'\n')
 im=Image.new('RGB',(1400,850),'#f6f8fc'); d=ImageDraw.Draw(im)
 d.text((55,35),title,font=font(31,True),fill='#142d45')
 d.text((55,81),'Проект архитектуры • DIP-9 • 20.10.2026',font=font(19),fill='#50677c')
 svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="850" viewBox="0 0 1400 850"><rect width="1400" height="850" fill="#f6f8fc"/>',f'<text x="55" y="62" font-size="31" font-family="Arial" fill="#142d45">{html.escape(title)}</text>']
 for x1,y1,x2,y2,label in edges:
  d.line((x1,y1,x2,y2),fill='#6d849a',width=3)
  a=math.atan2(y2-y1,x2-x1); pts=[(x2,y2),(x2-15*math.cos(a-.45),y2-15*math.sin(a-.45)),(x2-15*math.cos(a+.45),y2-15*math.sin(a+.45))]; d.polygon(pts,fill='#6d849a')
  svg.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#6d849a" stroke-width="3"/><polygon points="'+ ' '.join(f'{x},{y}' for x,y in pts)+'" fill="#6d849a"/>')
  if label:
   mx,my=(x1+x2)/2,(y1+y2)/2; w=d.textlength(label,font=font(18)); d.rectangle((mx-w/2-6,my-25,mx+w/2+6,my-1),fill='#f6f8fc'); d.text((mx-w/2,my-25),label,font=font(18),fill='#38516a')
   svg.append(f'<text x="{mx}" y="{my-8}" text-anchor="middle" font-size="18" font-family="Arial">{html.escape(label)}</text>')
 for x,y,w,h,lines in nodes:
  d.rounded_rectangle((x,y,x+w,y+h),radius=16,fill='white',outline='#b3c7d6',width=2)
  svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="white" stroke="#b3c7d6"/>')
  for i,l in enumerate(lines):
   yy=y+22+i*32; tw=d.textlength(l,font=font(22,i==0)); d.text((x+(w-tw)/2,yy),l,font=font(22,i==0),fill='#142d45')
   svg.append(f'<text x="{x+w/2}" y="{yy+22}" text-anchor="middle" font-family="Arial" font-size="22" fill="#142d45">{html.escape(l)}</text>')
 d.text((55,803),'Исследовательский прототип. Компоненты ещё не реализованы.',font=font(19),fill='#50677c')
 im.save(ROOT/f'diagrams/export/{name}.png'); svg.append('</svg>'); (ROOT/f'diagrams/export/{name}.svg').write_text(''.join(svg))
diagram('context','Контекст системы',[(60,220,280,130,['Врач / оператор','Загрузка и просмотр']),(500,220,380,160,['DR Grading Assistant','Градация • уверенность','Бинарный флаг • карта']),(1050,220,290,130,['Автор проекта','Обучение и проверка']),(500,570,380,130,['Открытые наборы данных','APTOS / EyePACS','IDRiD / Messidor-2'])],[(340,280,500,280,'снимок'),(500,340,340,340,'ответ'),(1050,280,880,280,'версия модели'),(690,570,690,380,'offline-оценка')],'''flowchart LR
 U[Врач / оператор] -->|снимок| S[DR Grading Assistant]
 S -->|градация, уверенность, бинарный флаг, карта| U
 A[Автор проекта] -->|версия модели| S
 D[Открытые данные] -->|offline-обучение и оценка автором| S''')
diagram('use-case','Варианты использования',[(45,320,260,110,['Врач / оператор']),(480,155,450,110,['UC-01: загрузить снимок']),(480,355,450,140,['UC-02: изучить результат','Стадия, уверенность, карта']),(480,585,450,110,['UC-03: исправить ошибку']),(1050,355,300,140,['Автор проекта','UC-04: оценить модель'])],[(305,370,480,210,''),(305,380,480,420,''),(305,400,480,635,''),(1050,425,930,425,'версия модели')],'''flowchart LR
 U[Врач / оператор] --- C1([UC-01 Загрузить снимок])
 U --- C2([UC-02 Изучить результат])
 U --- C3([UC-03 Исправить ошибку])
 A[Автор проекта] --- C4([UC-04 Оценить и выпустить модель])
 C4 -->|версия модели для результата| C2''')
diagram('components','Компоненты и поток данных',[(60,165,260,110,['Web UI','HTML / JS']),(495,165,350,110,['FastAPI','Валидация загрузки']),(1030,165,300,110,['Предобработка','crop / resize / norm']),(1030,410,300,140,['PyTorch CNN','Logits + Grad-CAM']),(495,410,350,140,['Постобработка','Температура / порог','Контракт ответа']),(60,410,260,140,['Результат UI','Стадия и флаг','Уверенность / карта']),(495,660,350,100,['Артефакты версии','Веса / T / порог / config'])],[(320,220,495,220,'файл'),(845,220,1030,220,'RGB'),(1180,275,1180,410,'tensor'),(1030,480,845,480,'logits / карта'),(495,480,320,480,'JSON'),(670,660,670,550,'T / порог'),(845,710,1180,550,'веса')],'''flowchart LR
 UI[Web UI] -->|файл| API[FastAPI / валидация]
 API -->|RGB| PRE[Предобработка]
 PRE -->|tensor| CNN[PyTorch CNN и Grad-CAM]
 CNN -->|logits и карта| POST[Постобработка / T / порог]
 POST -->|JSON| OUT[Экран результата]
 ART[Артефакты версии] -->|веса| CNN
 ART -->|T и порог| POST''')
# These are schematic design exports, not screenshots of an implemented medical service.
for state in ['upload','result','error']:
 im=Image.new('RGB',(1400,950),'#f3f7fa'); d=ImageDraw.Draw(im)
 d.rectangle((0,0,1400,105),fill='#14364c'); d.text((60,30),'DR Grading Assistant',font=font(32,True),fill='white'); d.text((1030,42),'МАКЕТ • НЕ МОДЕЛЬ',font=font(20),fill='#8ed9df')
 d.rounded_rectangle((70,140,1330,220),radius=12,fill='#fff3d8'); d.text((95,158),'Исследовательский прототип. Результат не является диагнозом.',font=font(24),fill='#735220')
 d.text((90,245),{'upload':'Загрузите снимок глазного дна','result':'Исследовательская оценка','error':'Не удалось прочитать файл'}[state],font=font(36,True),fill='#18384e')
 if state=='upload':
  d.rounded_rectangle((90,330,1310,680),radius=22,fill='white',outline='#aac6d2',width=3)
  d.text((410,420),'Выберите один JPG или PNG',font=font(30,True),fill='#18384e'); d.text((455,475),'До 20 MiB • обезличенный снимок',font=font(23),fill='#5f778b'); d.rounded_rectangle((520,550,880,615),radius=12,fill='#12667a'); d.text((580,565),'Выбрать файл',font=font(27,True),fill='white')
  d.text((95,735),'Состояния: файл выбран → обработка → результат / ошибка',font=font(23),fill='#5f778b')
 elif state=='result':
  d.rounded_rectangle((90,330,590,735),radius=20,fill='#e4edf1'); d.text((145,480),'Место для снимка и карты',font=font(26),fill='#466778'); d.text((148,525),'Изображение не подставлено',font=font(22),fill='#466778')
  for i,l in enumerate(['Пример: стадия 2 — умеренная ДР','Демонстрационная уверенность: 68%','Калибровка: не выполнена','Score DR >= 2: 0,74 • порог: 0,50','Флаг: положительный','Числа условные, модель не запускалась']): d.text((650,340+60*i),l,font=font(24,i==0),fill='#18384e')
  d.text((90,775),'Отрицательный флаг не исключает другие заболевания и макулярный отёк.',font=font(23),fill='#5f778b')
 else:
  d.rounded_rectangle((90,330,1310,650),radius=20,fill='white',outline='#deaf9d',width=2)
  d.text((130,380),'Файл повреждён или формат не поддерживается',font=font(30,True),fill='#8b3f2a'); d.text((130,445),'Выберите другой JPG/PNG. Исследовательская оценка не выполнялась.',font=font(24),fill='#5f778b'); d.rounded_rectangle((130,525,530,595),radius=12,fill='#12667a'); d.text((165,545),'Выбрать другой файл',font=font(26,True),fill='white')
 d.text((90,885),'DIP-10 • Макет интерфейса • 20.10.2026',font=font(20),fill='#5f778b'); im.save(ROOT/f'docs/ux/{state}.png')
