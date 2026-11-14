{
    "name": "Brocode Barbershop",
    "summary": "Sistem Informasi Manajemen Brocode Barbershop Terintegrasi",
    "version": "17.0.1.0.0",
    "author": "IF3141 - Kelompok 03",
    "category": "Services",
    "depends": ["base", "mail"],
    "application": True,
    "installable": True,
    "data": [
        "security/ir.model.access.csv",
        "views/reservation_views.xml",       # <--- Pindahkan view ke atas
        "views/store_readiness_views.xml",   # <--- Pindahkan view ke atas
        "views/menus.xml",                   # <--- Pindahkan menu ke bawah
    ],
}