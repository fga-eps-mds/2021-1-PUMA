import ipywidgets as widgets

def loading(_max, _min=0, _val=0):
  return widgets.FloatProgress(
      value=_val,
      min=_min,
      max=_max,
      description='Loading:',
      bar_style='success',
      style={'bar_color': '#0000ff'},
      orientation='horizontal'
  )

def update(prog):
  prog.value += 1
  if prog.value == prog.max:
    prog.close()
