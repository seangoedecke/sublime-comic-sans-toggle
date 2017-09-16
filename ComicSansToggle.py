import sublime
import sublime_plugin

class ComicSansToggleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    current_font = self.view.settings().get('font_face')
    if current_font == 'Comic Sans MS':
      # revert to global font_face setting
      self.view.settings().erase('font_face')
    else:
      self.view.settings().set('font_face', 'Comic Sans MS')
