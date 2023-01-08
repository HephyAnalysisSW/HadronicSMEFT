import os

if os.environ['USER'] in ['robert.schoefbeck']:

    skim_output_directory               = "/scratch-cbe/users/robert.schoefbeck/HadronicSMEFT/postprocessed/"
    plot_directory                      = "/groups/hephy/cms/robert.schoefbeck/www/HadronicSMEFT/"

    gridpack_directory                  = "/eos/vbc/user/robert.schoefbeck/gridpacks/"
    cache_directory                     = "/users/robert.schoefbeck/public/cache/HadronicSMEFT/"


elif os.environ['USER'] in ['oskar.rothbacher']:

    skim_output_directory               = "/groups/hephy/cms/oskar.rothbacher/HadronicSMEFT/postprocessed/"
    plot_directory                      = "/groups/hephy/cms/oskar.rothbacher/www/HadronicSMEFT/"

    gridpack_directory                  = "/eos/vbc/user/robert.schoefbeck/gridpacks/"
    cache_directory                     = "/users/robert.schoefbeck/public/cache/HadronicSMEFT/"

elif os.environ['USER'] in ['dietrich.liko']:

    skim_output_directory               = "/groups/hephy/cms/dietrich.liko/HadronicSMEFT/postprocessed/"
    plot_directory                      = "/groups/hephy/cms/dietrich.liko/www/HadronicSMEFT/"

    gridpack_directory                  = "/eos/vbc/user/robert.schoefbeck/gridpacks/"
    cache_directory                     = "/users/robert.schoefbeck/public/cache/HadronicSMEFT/"
