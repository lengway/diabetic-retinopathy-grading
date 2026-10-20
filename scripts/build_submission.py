"""Build a traceable Russian report and a separate PDF of actual YouTrack captures."""
from pathlib import Path
import re,html,json
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,Image,KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER
from PIL import Image as PILImage
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'output/pdf';OUT.mkdir(parents=True,exist_ok=True)
for name,f in [('Arial','Arial.ttf'),('Arial-Bold','Arial Bold.ttf'),('Arial-Italic','Arial Italic.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/System/Library/Fonts/Supplemental/'+f))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial-Italic',boldItalic='Arial-Bold')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyRU',fontName='Arial',fontSize=9.3,leading=13.2,spaceAfter=7,splitLongWords=True))
styles.add(ParagraphStyle(name='SmallRU',parent=styles['BodyRU'],fontSize=7.5,leading=10,spaceAfter=2))
styles.add(ParagraphStyle(name='H1RU',fontName='Arial-Bold',fontSize=18,leading=23,spaceAfter=14,spaceBefore=9,keepWithNext=True))
styles.add(ParagraphStyle(name='H2RU',fontName='Arial-Bold',fontSize=12,leading=16,spaceAfter=8,spaceBefore=10,keepWithNext=True))
styles.add(ParagraphStyle(name='TitleRU',fontName='Arial-Bold',fontSize=23,leading=30,alignment=TA_CENTER,spaceAfter=22))
W,H=595.28,841.89; WIDTH=W-100

def clean(s):
 s=s.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')
 s=html.escape(s)
 s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'`([^`]+)`',r'\1',s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m: '<link href="'+m[2]+'" color="#14627a">'+m[1]+'</link>' if m[2].startswith('http') else m[1],s)
 s=re.sub(r'(?<![="\w])(https?://[^\s<]+)',lambda m:'<link href="'+m[1]+'" color="#14627a">'+m[1]+'</link>',s) if '<link' not in s else s
 return s

def para(s,style='BodyRU'): return Paragraph(clean(s),styles[style])
def picture(path,maxh=350):
 with PILImage.open(path) as im: iw,ih=im.size
 scale=min(WIDTH/iw,maxh/ih);return Image(str(path),width=iw*scale,height=ih*scale)
def md(path):
 lines=path.read_text().splitlines(); items=[];i=0;buf=[];code=False
 def flush():
  if buf:items.append(para(' '.join(buf)));buf.clear()
 while i<len(lines):
  s=lines[i].strip()
  if s.startswith('```'): flush();code=not code;i+=1;continue
  if code: i+=1;continue
  if s.startswith('|'):
   flush(); rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    parts=[a.strip() for a in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r'[-: ]+',a or '-') for a in parts): rows.append(parts)
    i+=1
   count=max(map(len,rows)); rows=[r+['']*(count-len(r)) for r in rows]
   widths=[WIDTH/count]*count
   if count==4:widths=[WIDTH*.15,WIDTH*.23,WIDTH*.30,WIDTH*.32]
   if count==5:widths=[WIDTH*.10,WIDTH*.18,WIDTH*.25,WIDTH*.25,WIDTH*.22]
   if count==6:widths=[WIDTH*.13,WIDTH*.16,WIDTH*.19,WIDTH*.24,WIDTH*.16,WIDTH*.12]
   t=Table([[para(c,'SmallRU') for c in r] for r in rows],colWidths=widths,repeatRows=1,hAlign='LEFT',splitByRow=1,splitInRow=1)
   t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e6eff4')),('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),.3,colors.HexColor('#c8d5dd')),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f8fafb')])]))
   items.extend([t,Spacer(1,10)]);continue
  match=re.fullmatch(r'!\[([^]]*)\]\(([^)]+)\)',s)
  if match:
   flush();img=(path.parent/match[2]).resolve();items.extend([picture(img),para(match[1],'SmallRU'),Spacer(1,10)])
  elif s.startswith('# '):flush();items.append(para(s[2:],'H1RU'))
  elif s.startswith('## '):flush();items.append(para(s[3:],'H2RU'))
  elif s.startswith('### '):flush();items.append(para(s[4:],'H2RU'))
  elif s in ['---','']:flush()
  elif s.startswith('- '):flush();items.append(para('• '+s[2:]))
  else:buf.append(s)
  i+=1
 flush();return items

def footer(c,doc):
 c.saveState();c.setFont('Arial',8);c.setFillColor(colors.HexColor('#617686'));c.drawString(50,27,'Кутбеев Р.В. | Апробация | 20.10.2026');c.drawRightString(W-50,27,str(doc.page));c.restoreState()
def build(name,story):
 SimpleDocTemplate(str(OUT/name),pagesize=(W,H),rightMargin=50,leftMargin=50,topMargin=45,bottomMargin=46,title=name[:-4],author='Кутбеев Роман Владимирович',allowSplitting=True).build(story,onFirstPage=footer,onLaterPages=footer)
files=['docs/proposal.md','docs/evidence-of-relevance.md','docs/literature-review.md','docs/systems-comparison.md','docs/technology-comparison.md','docs/requirements.md','docs/architecture.md','docs/ux/README.md','docs/verification-plan.md','docs/project-management.md','docs/supervisor-feedback.md','docs/data-plan.md','docs/submission/README.md']
story=[Spacer(1,50),para('Astana IT University','H2RU'),para('Школа программной инженерии'),Spacer(1,35),para('ОТЧЁТ К АПРОБАЦИОННОМУ ПЕРИОДУ','TitleRU'),para('Разработка интеллектуального ассистента для градации диабетической ретинопатии по снимкам глазного дна','H1RU'),Spacer(1,25),para('Исполнитель: Кутбеев Роман Владимирович, SE-2404'),para('Руководитель: Турарова Маржан Кабдыкалиевна'),para('Индивидуальный дипломный проект • Software Engineering'),Spacer(1,25),para('Рабочая версия 0.2 от 20 октября 2026 года. Подготовлены аналитические и проектные материалы. Пользовательские беседы, EDA и новый отзыв руководителя остаются открытыми. Реализация модели и сервиса запланирована.'),para('Исследовательский прототип. Не предназначен для клинической диагностики.'),Spacer(1,18),para('Астана, 2026'),PageBreak(),para('Состав отчёта','H1RU')]
for i,n in enumerate(files):
 title=(ROOT/n).read_text().splitlines()[0].lstrip('# ')
 if i==0:title='1. Постановка задачи и project proposal'
 story.append(para(title))
story.extend([Spacer(1,20),para('Сведения о готовности','H2RU'),para('Настоящий файл объединяет все разделы из списка требований, сохранённого в контексте проекта. Наличие раздела не означает выполнение его внешних условий. Отдельный официальный файл регламента не предоставлен; окончательное соответствие необходимо сверить до сдачи.'),para('Документация сопровождает реальные файлы репозитория; снимки доски и задач вынесены в отдельный PDF. Поля формы подготовлены отдельно. Форму студент подаёт один раз до 18:00 24.10.2026.')])
for n in files:story.append(PageBreak());story.extend(md(ROOT/n))
build('Отчет_апробация_Кутбеев_2026-10-20.pdf',story)
shots=sorted((ROOT/'docs/submission/screenshots').glob('*.png'))
if shots:
 s=[para('YouTrack: доска и задачи','H1RU'),para('Кутбеев Роман Владимирович, SE-2404. Проект DIP. Реальные снимки интерфейса от 20.10.2026. На снимках отражены состояния задач на момент съёмки; незавершённые задачи не выдаются за выполненные.'),para('https://diabeticretinopathygrading.youtrack.cloud/agiles/204-1/current'),para('Доступ комиссии к сайту и отдельным задачам нужно проверить отдельно. Скриншоты не заменяют доступ по ссылке.')]
 for f in shots:
  s.extend([PageBreak(),para(f.stem,'H2RU'),picture(f,640)])
 build('YouTrack_Кутбеев_2026-10-20.pdf',s)
print('Built report; screenshot pages:',len(shots))
