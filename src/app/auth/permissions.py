# ==================================================
# ROLE PERMISSIONS
# ==================================================

ROLE_PERMISSIONS = {

    "admin": [

        "home",
        "dashboard",
        "brands",
        "pipeline",
        "qa",
        "forecast",
        "anomaly"

    ],

    "ejecutivo": [

        "home",
        "dashboard",
        "brands"

    ],

    "qa": [

        "home",
        "qa"

    ],

    "operaciones": [

        "home",
        "pipeline"

    ]

}


# ==================================================
# VALIDATE PERMISSION
# ==================================================

def has_permission(

    role,
    permission

):

    return permission in ROLE_PERMISSIONS.get(

        role,
        []

    )