from django.http import JsonResponse
import pathlib

taxa_worms_cache = None  # Global.

# Dummy view for testing purposes
def get_taxon(request, aphia_id):
    all_taxa = get_taxon_list()
    try:
        taxon = next(filter(lambda t: t["aphiaId"] == str(aphia_id), all_taxa))
        return JsonResponse(taxon)
    except StopIteration:
        return JsonResponse({"message": "Taxon not found"}, status=404)


# Dummy view for testing purposes
def get_taxa(request):
    return JsonResponse({"taxa": get_taxon_list()})


# Dummy view for testing purposes
def get_taxa_by_filter(request):
    return JsonResponse({"taxa": get_taxon_list()})


# Dummy view for testing purposes
def get_taxa_by_name(request):
    name = request.GET.get("name", "").lower()
    taxa = list(
        filter(lambda t: name in t["scientificName"].lower(), get_taxon_list(),)
    )
    return JsonResponse({"taxa": taxa})


# Dummy view for testing purposes
def get_taxa_by_parent(request):
    aphia_id = str(request.GET.get("aphiaId", "0"))
    taxa = list(filter(lambda t: aphia_id == t["parentId"], get_taxon_list(),))
    return JsonResponse({"taxa": taxa})


def get_taxon_list():
    """ """
    global taxa_worms_cache
    if taxa_worms_cache is not None:
        return taxa_worms_cache

    taxa_worms_path = pathlib.Path("../nua-content/species", "taxa_worms.txt")
    # Use test data if not available. TODO: Remove later.
    if not taxa_worms_path.exists():
        taxa_worms_cache = get_test_taxon_list()
        return taxa_worms_cache

    rename_header = {
        "aphia_id": "aphiaId",
        "parent_name": "parentName",
        "parent_id": "parentId",
        "scientific_name": "scientificName",
    }
    try:
        taxa_worms_cache = []
        with taxa_worms_path.open("r", encoding="cp1252", errors="ignore") as in_file:
            header = None
            for row in in_file:
                row = [item.strip() for item in row.strip().split("\t")]
                if row:
                    if header is None:
                        header = [rename_header.get(item, item) for item in row]
                    else:
                        row_dict = dict(zip(header, row))
                        scientific_name = row_dict.get("scientificName", "")
                        if scientific_name:
                            taxa_worms_cache.append(row_dict)
        print("DEBUG: Taxon list length: ", len(taxa_worms_cache))
        return taxa_worms_cache
    except Exception as e:
        print("DEBUG: Exception in get_taxon_list: ", e)
        return []


def get_test_taxon_list():
    return [
        {
            "scientificName": "Acantharia",
            "rank": "Class",
            "aphiaId": "586732",
            "parentName": "Radiozoa",
            "parentId": "582421",
            "authority": "",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
        },
        {
            "scientificName": "Acantharia incertae sedis",
            "rank": "Order",
            "aphiaId": "711964",
            "parentName": "Acantharia",
            "parentId": "586732",
            "authority": "",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Acantharia incertae sedis",
        },
        {
            "scientificName": "Acanthonida",
            "rank": "Order",
            "aphiaId": "866438",
            "parentName": "Acantharia",
            "parentId": "586732",
            "authority": "Haeckel, 1881",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Acanthonida",
        },
        {
            "scientificName": "Astrolonchidae",
            "rank": "Family",
            "aphiaId": "866439",
            "parentName": "Acanthonida",
            "parentId": "866438",
            "authority": "Haeckel, 1881",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Acanthonida",
            "family": "Astrolonchidae",
        },
        {
            "scientificName": "Zygacanthida",
            "rank": "Subfamily",
            "aphiaId": "866440",
            "parentName": "Astrolonchidae",
            "parentId": "866439",
            "authority": "Haeckel",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Acanthonida",
            "family": "Astrolonchidae",
        },
        {
            "scientificName": "Acanthonia",
            "rank": "Genus",
            "aphiaId": "866441",
            "parentName": "Zygacanthida",
            "parentId": "866440",
            "authority": "Haeckel, 1881",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Acanthonida",
            "family": "Astrolonchidae",
            "genus": "Acanthonia",
        },
        {
            "scientificName": "Acanthonia echinoides",
            "rank": "Species",
            "aphiaId": "866442",
            "parentName": "Acanthonia",
            "parentId": "866441",
            "authority": "(Claparède & Lachmann, 1858) Haeckel, 1881",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Acanthonida",
            "family": "Astrolonchidae",
            "genus": "Acanthonia",
        },
        {
            "scientificName": "Arthracanthida",
            "rank": "Order",
            "aphiaId": "367301",
            "parentName": "Acantharia",
            "parentId": "586732",
            "authority": "Schewiakoff, 1926",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
        },
        {
            "scientificName": "Acanthostaurus",
            "rank": "Genus",
            "aphiaId": "393198",
            "parentName": "Arthracanthida",
            "parentId": "367301",
            "authority": "Haeckel, 1862",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "",
            "genus": "Acanthostaurus",
        },
        {
            "scientificName": "Acanthostaurus nordgaardi",
            "rank": "Species",
            "aphiaId": "393199",
            "parentName": "Acanthostaurus",
            "parentId": "393198",
            "authority": "Jørgensen, 1899",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "",
            "genus": "Acanthostaurus",
        },
        {
            "scientificName": "Acanthostaurus pallidus",
            "rank": "Species",
            "aphiaId": "866443",
            "parentName": "Acanthostaurus",
            "parentId": "393198",
            "authority": "(Claparède & Lachmann, 1858) Haeckel, 1862",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "",
            "genus": "Acanthostaurus",
        },
        {
            "scientificName": "Phyllacantha",
            "rank": "Suborder",
            "aphiaId": "367303",
            "parentName": "Arthracanthida",
            "parentId": "367301",
            "authority": "Schewiakoff, 1926",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
        },
        {
            "scientificName": "Dictyacanthidae",
            "rank": "Family",
            "aphiaId": "367337",
            "parentName": "Phyllacantha",
            "parentId": "367303",
            "authority": "Schewiakoff, 1926",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Dictyacanthidae",
        },
        {
            "scientificName": "Phyllostauridae",
            "rank": "Family",
            "aphiaId": "367335",
            "parentName": "Phyllacantha",
            "parentId": "367303",
            "authority": "Schewiakoff, 1926",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Phyllostauridae",
        },
        {
            "scientificName": "Stauracanthidae",
            "rank": "Infraorder",
            "aphiaId": "367336",
            "parentName": "Phyllacantha",
            "parentId": "367303",
            "authority": "Schewiakoff, 1926",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
        },
        {
            "scientificName": "Sphaenacantha",
            "rank": "Suborder",
            "aphiaId": "367302",
            "parentName": "Arthracanthida",
            "parentId": "367301",
            "authority": "Schewiakoff, 1926",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
        },
        {
            "scientificName": "Acanthometridae",
            "rank": "Family",
            "aphiaId": "235748",
            "parentName": "Sphaenacantha",
            "parentId": "367302",
            "authority": "Haeckel, 1887",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Acanthometridae",
        },
        {
            "scientificName": "Acanthometra",
            "rank": "Genus",
            "aphiaId": "235749",
            "parentName": "Acanthometridae",
            "parentId": "235748",
            "authority": "J. Müller, 1856",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Acanthometridae",
            "genus": "Acanthometra",
        },
        {
            "scientificName": "Acanthometra pellucida",
            "rank": "Species",
            "aphiaId": "235750",
            "parentName": "Acanthometra",
            "parentId": "235749",
            "authority": "Müller, 1858",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Acanthometridae",
            "genus": "Acanthometra",
        },
        {
            "scientificName": "Acanthometron",
            "rank": "Genus",
            "aphiaId": "391880",
            "parentName": "Acanthometridae",
            "parentId": "235748",
            "authority": "",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Acanthometridae",
            "genus": "Acanthometron",
        },
        {
            "scientificName": "Acanthometron elastricum",
            "rank": "Species",
            "aphiaId": "391881",
            "parentName": "Acanthometron",
            "parentId": "391880",
            "authority": "",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Acanthometridae",
            "genus": "Acanthometron",
        },
        {
            "scientificName": "Acanthometron pellucida",
            "rank": "Species",
            "aphiaId": "391883",
            "parentName": "Acanthometron",
            "parentId": "391880",
            "authority": "",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Acanthometridae",
            "genus": "Acanthometron",
        },
        {
            "scientificName": "Amphilonche",
            "rank": "Genus",
            "aphiaId": "235751",
            "parentName": "Acanthometridae",
            "parentId": "235748",
            "authority": "",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Acanthometridae",
            "genus": "Amphilonche",
        },
        {
            "scientificName": "Amphilonche elongata",
            "rank": "Species",
            "aphiaId": "235752",
            "parentName": "Amphilonche",
            "parentId": "235751",
            "authority": "(Müller, 1858)",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Acanthometridae",
            "genus": "Amphilonche",
        },
        {
            "scientificName": "Diploconidae",
            "rank": "Family",
            "aphiaId": "367340",
            "parentName": "Sphaenacantha",
            "parentId": "367302",
            "authority": "Haeckel, 1887",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Diploconidae",
        },
        {
            "scientificName": "Dorataspidae",
            "rank": "Family",
            "aphiaId": "367338",
            "parentName": "Sphaenacantha",
            "parentId": "367302",
            "authority": "Haeckel, 1887",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Dorataspidae",
        },
        {
            "scientificName": "Hexalaspidae",
            "rank": "Family",
            "aphiaId": "367342",
            "parentName": "Sphaenacantha",
            "parentId": "367302",
            "authority": "Haeckel, 1887",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Hexalaspidae",
        },
        {
            "scientificName": "Lithopteridae",
            "rank": "Family",
            "aphiaId": "367341",
            "parentName": "Sphaenacantha",
            "parentId": "367302",
            "authority": "Haeckel, 1887",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Lithopteridae",
        },
        {
            "scientificName": "Phractopeltidae",
            "rank": "Family",
            "aphiaId": "367339",
            "parentName": "Sphaenacantha",
            "parentId": "367302",
            "authority": "Haeckel, 1887",
            "status": "accepted",
            "kingdom": "Chromista",
            "phylum": "Radiozoa",
            "class": "Acantharia",
            "order": "Arthracanthida",
            "family": "Phractopeltidae",
        },
    ]
