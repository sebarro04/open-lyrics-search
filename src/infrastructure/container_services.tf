resource "azurerm_service_plan" "main" {
  name                = "main-${var.group}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "S1"
}
resource "azurerm_linux_web_app" "main" {
  name                = "main-${var.group}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id
  identity {
    type         = "UserAssigned"
    identity_ids = [azurerm_user_assigned_identity.main.id]
  }
  app_settings = {
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE"   = "false",
    "AZURE_CLIENT_ID"                       = "${azurerm_user_assigned_identity.main.client_id}",
    "REACT_APP_FIREBASE_APIKEY"             = "AIzaSyBziU3JDNvYWVuZWSEAZdlOw0aCpj3MoAw",
    "REACT_APP_FIREBASE_AUTHDOMAIN"         = "openlyrics-search-83331.firebaseapp.com",
    "REACT_APP_FIREBASE_PROJECTID"          = "openlyrics-search-83331",
    "REACT_APP_FIREBASE_STORAGEBUCKET"      = "openlyrics-search-83331.appspot.com",
    "REACT_APP_FIREBASE_MESSAGINGSENDERID"  = "677278551417",
    "REACT_APP_FIREBASE_APPID"              = "1:677278551417:web:2181987b961ce3e57e33a8"
  }
  site_config {
    application_stack {
      docker_image     = "erick13as/react-app"
      docker_image_tag = "latest"
    }
  }
}

