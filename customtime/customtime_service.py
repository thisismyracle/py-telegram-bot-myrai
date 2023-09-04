from time import localtime, strftime

days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jum\'at', 'Sabtu', 'Minggu']
months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']


class CustomTime:

    @classmethod
    def get_time_context(cls):
        day = days[localtime().tm_wday]
        month = months[(localtime().tm_mon - 1)]

        hour = localtime().tm_hour

        time_affix = 'malam'
        if hour < 5:
            time_affix = 'dini hari'
        elif hour < 11:
            time_affix = 'pagi'
        elif hour < 15:
            time_affix = 'siang'
        elif hour < 18:
            time_affix = 'sore'
        elif hour < 19:
            time_affix = 'maghrib'

        return strftime(f'Sekarang adalah hari {day}, tanggal %d {month} %Y, jam %H:%M {time_affix}.', localtime())
