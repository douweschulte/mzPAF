import re

pattern = re.compile(r"""^(?P<is_auxiliary>&)?
   (?:(?P<analyte_reference>\d+)@)?
   (?:(?:(?P<series>[axbycz]\.?)(?P<ordinal>\d+)(?:\{(?P<sequence_ordinal>.+)\})?)|
   (?P<series_internal>[m](?P<internal_start>\d+):(?P<internal_end>\d+)(?:\{(?P<sequence_internal>.+)\})?)|
   (?P<precursor>p)|
   (:?I(?P<immonium>[ARNDCEQGHKMFPSTWYVIL])(?:\[(?P<immonium_modification>(?:[^\]]+))\])?)|
   (?P<reference>r(?:
    (?:\[
        (?P<reference_label>[^\]]+)
    \])
   ))|
   (?:f\{(?P<formula>[A-Za-z0-9]+)\})|
   (?:_\{
    (?P<external_ion>[^\{\}\s,/]+)
    \})|
   (?:s\{(?P<smiles>[^\}]+)\})|
   (?:(?P<unannotated>\?)(?P<unannotated_label>\d+)?)
)
(?P<neutral_losses>(?:[+-]\d*
    (?:(?:[A-Z][A-Za-z0-9]*)|
        (?:\[
            (?:
                (?:[A-Za-z0-9:\.]+)
            )
            \])
    )
)+)?
(?:(?P<isotope>[+-]\d*)i)?
(?:\[(?P<adducts>M(:?[+-]\d*[A-Z][A-Za-z0-9]*)+)\])?
(?:\^(?P<charge>[+-]?\d+))?
(?:/(?P<mass_error>[+-]?\d+(?:\.\d+)?)(?P<mass_error_unit>ppm)?)?
(?:\*(?P<confidence>\d*(?:\.\d+)?))?""", re.X)