from faker import Faker
import random


def fakeidy():
    fake = Faker('fr_FR')
    name = fake.name()
    address = fake.address().replace('\n', ', ')
    if random.randint(0, 1) == 0:
        mail = name.replace(' ', '.').lower() + "@" + fake.free_email_domain()
    else:
        mail = name.replace(' ', '').lower() + "@" + fake.free_email_domain()
    telephone = fake.phone_number()
    entreprise = fake.company()
    taf = fake.job()
    secu = fake.ssn()
    ip = fake.ipv4()
    naissance = fake.date_of_birth()
    mac_address = fake.mac_address()
    iban = fake.iban()
    credit_card_expire = fake.credit_card_expire()
    credit_card_provider = fake.credit_card_provider()
    credit_card = fake.credit_card_number()
    credit_card_security_code = fake.credit_card_security_code()
    complete_credit_card = name + "\n     ↳ Type de carte: " + credit_card_provider + "\n     ↳ Numéro de carte: " + credit_card + "\n     ↳ Date d'expiration: " + credit_card_expire + "\n     ↳ Code CSV: " + credit_card_security_code
    return("👤 | Nom : " + name + "\n🎂 | Date de naissance : " + str(naissance) + "\n📧 | Mail : " + mail + "\n📞 | Téléphone : " + telephone + "\n🏢 | Entreprise : " + entreprise + "\n👔 | Profession : " + taf + "\n🔒 | Numéro de sécurité sociale : " + secu + "\n🏦 | IBAN : " + iban + "\n💳 | Carte de crédit : " + complete_credit_card + "\n🌐 | Adresse IP : " + ip + "\n📱 | Adresse MAC : " + mac_address + "\n🏠 | Adresse : " + address)