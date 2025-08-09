# Konstanta waktu memanggang (wajib)
EXPECTED_BAKE_TIME = 40

# Konstanta waktu persiapan (opsional)
# Menghindari penggunaan "magic numbers"
PREPARATION_TIME = 2  # menit per lapisan lasagna

print(EXPECTED_BAKE_TIME)


# TODO: Hapus 'pass' dan lengkapi fungsi di bawah ini
def bake_time_remaining(elapsed_bake_time):
    """
    Menghitung sisa waktu memanggang.

    :param elapsed_bake_time: int - waktu memanggang yang sudah berlalu.
    :return: int - sisa waktu memanggang (dalam menit), dihitung dari EXPECTED_BAKE_TIME.

    Fungsi ini menerima jumlah menit lasagna sudah berada di oven
    dan mengembalikan berapa menit lagi lasagna perlu dipanggang
    berdasarkan EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time



def preparation_time_in_minutes(number_of_layers):
    """
    Menghitung total waktu persiapan berdasarkan jumlah lapisan lasagna.

    :param number_of_layers: int - jumlah lapisan lasagna.
    :return: int - total waktu persiapan (dalam menit), berdasarkan PREPARATION_TIME.
    """
    return number_of_layers * PREPARATION_TIME



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Menghitung total waktu yang sudah dihabiskan.

    :param number_of_layers: int - jumlah lapisan lasagna.
    :param elapsed_bake_time: int - waktu memanggang yang sudah berlalu.
    :return: int - total waktu yang dihabiskan (persiapan + memanggang), dalam menit.
    """
    return (elapsed_bake_time) + number_of_layers * PREPARATION_TIME

