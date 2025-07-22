from django.core.management.base import BaseCommand
from cabinet.models import Icon, Link, Project

class Command(BaseCommand):
    help = 'Создает нужные проекты для home страницы'

    def handle(self, *args, **options):
        self.stdout.write("🔧 Исправляем проекты...")
        
        # Создаем/получаем иконки
        shop_icon, created = Icon.objects.get_or_create(
            name='shop',
            defaults={'icon': 'fas fa-shopping-cart'}
        )
        if created:
            self.stdout.write("✅ Создана иконка shop")
        
        blog_icon, created = Icon.objects.get_or_create(
            name='blog', 
            defaults={'icon': 'fas fa-blog'}
        )
        if created:
            self.stdout.write("✅ Создана иконка blog")
        
        # Создаем/получаем ссылки
        phantom_link, created = Link.objects.get_or_create(
            name='Phantom GitHub',
            defaults={'url': 'https://github.com/testMonzeN/PhantomTestWeb'}
        )
        if created:
            self.stdout.write("✅ Создана ссылка Phantom GitHub")
        
        blog_link, created = Link.objects.get_or_create(
            name='Blog GitHub',
            defaults={'url': 'https://github.com/testMonzeN/myfirstblog'}
        )
        if created:
            self.stdout.write("✅ Создана ссылка Blog GitHub")
        
        # Удаляем проекты с id 1 и 2 если они существуют
        deleted_count = Project.objects.filter(id__in=[1, 2]).count()
        if deleted_count > 0:
            Project.objects.filter(id__in=[1, 2]).delete()
            self.stdout.write(f"🗑 Удалено {deleted_count} старых проектов")
        
        # Создаем проект Blog Platform с id=1
        blog_project, created = Project.objects.get_or_create(
            id=1,
            defaults={
                'name': 'Blog Platform',
                'description': 'Блог-платформа с возможностью публикации статей, комментариев и категориями. Создан с использованием Django framework.',
                'type_icon': blog_icon,
                'links': blog_link
            }
        )
        if created:
            self.stdout.write("✅ Создан проект Blog Platform (ID: 1)")
        
        # Создаем проект Phantom Marketplace с id=2  
        phantom_project, created = Project.objects.get_or_create(
            id=2,
            defaults={
                'name': 'Phantom Marketplace',
                'description': 'Интернет-магазин с системой управления товарами, корзиной и оплатой. Полнофункциональная e-commerce платформа.',
                'type_icon': shop_icon,
                'links': phantom_link
            }
        )
        if created:
            self.stdout.write("✅ Создан проект Phantom Marketplace (ID: 2)")
        
        self.stdout.write(
            self.style.SUCCESS("\n🎉 Проекты готовы! Теперь ссылки на project_detail должны работать!")
        )