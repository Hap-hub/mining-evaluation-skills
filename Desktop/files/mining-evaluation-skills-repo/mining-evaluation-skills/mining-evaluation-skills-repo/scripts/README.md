# Scripts

All scripts here require real data supplied by the user. Do not invent inputs to make a
script "runnable" -- if data is missing, ask for it or give a qualitative answer instead.

## grade_tonnage_calculator.py
Computes a grade-tonnage sensitivity table from a composite/block CSV (columns: `grade`, `tonnage`).
```
python scripts/grade_tonnage_calculator.py data.csv --cutoffs 0.2,0.3,0.5,1.0 --grade-unit "% Cu"
```

## financial_model.py
Computes NPV, IRR, and payback from a cash-flow assumption JSON file, with an optional
one-variable sensitivity sweep.
```
python scripts/financial_model.py project.json --sensitivity revenue --range -0.2,-0.1,0,0.1,0.2
```

## resource_classification_checklist.py
A structured checklist (not an authoritative classifier) that flags inconsistencies between
a claimed resource category (Measured/Indicated/Inferred) and the supporting inputs given.
```
python scripts/resource_classification_checklist.py classification_inputs.json
```
