from odoo:12

ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8 
ADD addons/project_hicto /mnt/extra-addons/project_hicto
ADD addons/web /usr/lib/python3/dist-packages/odoo/addons/web
