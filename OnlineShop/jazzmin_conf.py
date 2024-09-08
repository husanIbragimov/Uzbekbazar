
JAZZMIN_SETTINGS = {

    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "UZBEKBAZAR Admin",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "UZBEKBAZAR",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "UZBEKBAZAR",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "assets/imgs/theme/header_logo.png",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "assets/imgs/theme/header_logo.png",
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "assets/imgs/theme/header_logo.png",
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-shape-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "assets/imgs/theme/header_logo.png",
    # Welcome text on the login screen
    "welcome_sign": "Welcome to the UZBEKBAZAR Admin",
    # Copyright on the footer
    "copyright": "ict-academy",
    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string
    "search_model": ["auth.User", "auth.Group"],
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": "{% if request.user.photo %}{{ request.user.photo.url }}{% else %}assets/imgs/theme/avatar.png{% endif %}",
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # external url that opens in a new window (Permissions can be added)
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"model": "auth.user"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": False,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # Whether to aut expand the menu
    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [
            {
                "name": "Make Messages",
                "url": "make_messages",
                "icon": "fas fa-comments",
                "permissions": ["books.view_book"],
            }
        ]
    },
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "accounts.User": "fas fa-user",
        "accounts.Organization": "fas fa-building",
        "base.BaseModel": "fas fa-square",
        "base.Variant": "fas fa-cube",
        "order.Wishlist": "fas fa-heart",  # Wishlist icon
        "order.ShopCart": "fas fa-shopping-cart",  # Shopping cart icon
        "order.Order": "fas fa-box",  # Order icon
        "order.OrderItem": "fas fa-box-open",  # Order item icon
        "order.OrderOneClick": "fas fa-mouse-pointer",  # One-click order icon
        "order.OrderVariant": "fas fa-tags",  # Order variant icon
        "order.OrderInfo": "fas fa-info-circle",
        "products.Size": "fas fa-ruler",  # Size icon
        "products.Category": "fas fa-folder-open",  # Category icon
        "products.Colors": "fas fa-palette",  # Colors icon
        "products.Brend": "fas fa-trademark",  # Brand icon
        "products.Season": "fas fa-cloud-sun",  # Season icon
        "products.AuthorBook": "fas fa-user-edit",  # Author icon
        "products.CoverBook": "fas fa-book-open",  # Book cover icon
        "products.PublisherBook": "fas fa-building",  # Publisher icon
        "products.LanguageBook": "fas fa-language",  # Language icon
        "products.Tags": "fas fa-tag",  # Tags icon
        "products.Volume_Xajm": "fas fa-book",  # Volume icon
        "products.Product": "fas fa-cube",  # Product icon
        "products.ProductImage": "fas fa-image",  # Product image icon
        "products.ProductSize": "fas fa-expand-arrows-alt",  # Product size icon
        "products.Additional_info": "fas fa-info",  # Additional information icon
        "products.ProductReview": "fas fa-star",  # Product review icon
        "products.Banner": "fas fa-flag",  # Banner icon
        "products.BannerDiscount": "fas fa-percent",  # Banner discount icon
        "products.DiscountDate": "fas fa-calendar-alt",  # Discount date icon
        "products.MonthlyBestSell": "fas fa-trophy",  # Monthly best sell icon
        "products.BannerBottom": "fas fa-arrow-down",  # Bottom banner icon


        
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-full-white",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "custom_admin.css",
    "custom_js": None,
    "custom_login_template": "admin/login.html",

    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "horizontal_tabs",
    },
    # Add a language dropdown into the admin
    # "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-lime",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "sandstone",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "login-logo":{
        "width": "10px",
        "height": "100px"
    }
}