import sublime
import sublime_plugin


class DayAndNightCommand(sublime_plugin.WindowCommand):
    def run(self, time):
        """
        Time will be 'day' or 'night'
        """
        user_settings = sublime.load_settings('Preferences.sublime-settings')
        plugin_default_settings = sublime.load_settings('DayAndNight.sublime-settings').get('day_and_night_defaults')

        user_settings.set('theme', plugin_default_settings.get(str(time) + '_theme'))
        user_settings.set('color_scheme', plugin_default_settings.get(str(time) + '_color_scheme'))

        sublime.save_settings("Preferences.sublime-settings")
