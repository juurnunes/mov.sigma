from django.db import models

class movimentos(models.Model):

    choices_unidade = (
        ("20", "20'"),
        ("40", "40'")
    )

    choices_tipo = (
        ("DRY", "DRY"),
        ("FR", "FLAT RACK"),
        ("HC", "HC"),
        ("OT", "OPEN TOP"),
        ("TK", "TANK"),
        ("RF", "REEFER")  

    )

    choices_modal = (
        ("I", "Importação"),
        ("E", "Exportação")
    )

    choices_estado = (
        ("C", "Cheio"),
        ("V", "Vazio")
    )

    container = models.CharField(max_length=15)
    unidade = models.CharField(max_length=2, choices=choices_unidade)
    tipo = models.CharField(max_length=3, choices=choices_tipo)
    lacre = models.CharField(max_length=30)
    modal = models.CharField(max_length=1, choices=choices_modal)
    estado = models.CharField(max_length=1, choices=choices_estado)
    observ = models.CharField(max_length=100, null=True)
    data_entrada = models.DateTimeField(null=False)
    data_saida = models.DateTimeField(null=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    usuario_alteracao = models.CharField(max_length= 30, null=True)
    usuario_inclusao = models.CharField(max_length= 30, null=True)


    def __str__ (self):
        return self.container
    




