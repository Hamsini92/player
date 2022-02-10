from django.contrib import admin
from playerlistings.models import Intuit
class FileAdmin(admin.ModelAdmin):
    list_display = ["player_id", "birth_country", "birth_state",
                    "birth_city",   "birthYear",
                    "birthMonth","birthDay",
                    "deathYear", "deathMonth",
                    "deathDay", "deathCountry",
                    "deathState","deathCity",
                    "nameFirst", "nameLast",
                    "nameGiven", "weight",
                    "height", "bats",
                    "throws", "debut",
                    "finalGame", "retroID",
                    "bbrefID"
                    ]


admin.site.register(Intuit, FileAdmin)