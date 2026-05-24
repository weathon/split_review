# Multi requery test

## Final Merger checkpoint

Old: `gen-1779424157-fG8t5s745dTsydhVFmBz` provider `GMICloud` endpoint `e9b742d8-f524-4795-8d84-0d5815e9b73b` score `6.0` decision `Accept` len `13314`

| run | response | provider | endpoint | completion | reasoning | len | sim_to_old | score | decision |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| previous_requery | `gen-1779490650-8cVgWJ0co7pR2gUcHfGL` | GMICloud (status 200) | `e9b742d8-f524-4795-8d84-0d5815e9b73b` | 2630 | 223 | 9380 | 0.1660 | 6.0 | Accept |
| new_requery_1 | `gen-1779491098-IjeKe5zmstSG6PchyGUU` | None (status 404) | `None` | None | None | 9527 | 0.1236 | 6.0 | Accept |
| new_requery_2 | `gen-1779491123-DC320qTLwAmG2Y30vIOb` | GMICloud (status 200) | `934a69f9-bd54-474b-beca-24560f721e12` | 3044 | 195 | 11805 | 0.1947 | 6.0 | Accept |
| new_requery_3 | `gen-1779491150-JFGnKUP55W88HZ027sSP` | GMICloud (status 200) | `e9b742d8-f524-4795-8d84-0d5815e9b73b` | 2704 | 153 | 10550 | 0.1303 | 6.0 | Accept |
| new_requery_4 | `gen-1779491175-xUpR83jadzJ43jGbw3yN` | GMICloud (status 200) | `e9b742d8-f524-4795-8d84-0d5815e9b73b` | 2781 | 280 | 10119 | 0.1305 | 6.0 | Accept |

## Calibration query-generation stages

### Stage 1 record 12

Old args:

```json
{
  "queries": [
    {
      "query": "few-shot anomaly detection multimodal",
      "high_score": 3.5,
      "low_score": -1,
      "n": 4
    },
    {
      "query": "prototype-based anomaly detection few-shot",
      "high_score": 7.5,
      "low_score": 3.5,
      "n": 4
    },
    {
      "query": "multimodal anomaly detection optimal transport prototype",
      "low_score": 7.5,
      "high_score": 11,
      "n": 4
    }
  ]
}
```

Old trace anchors: `bESxQeXTlo, MbtUctg3KW, O0vy7hHqyU, 3ZdGSTxKuy, Vi6p2TeujL, gTsLBDMZrL, J2we1sVd9m, 8TBGdH3t6a, cJs4oE4m9Q, TPZRq4FALB, 9Cu8MRmhq2, cNmu0hZ4CL`

Old args replayed now anchors: `bESxQeXTlo, MbtUctg3KW, O0vy7hHqyU, 3ZdGSTxKuy, Vi6p2TeujL, gTsLBDMZrL, J2we1sVd9m, 8TBGdH3t6a, cJs4oE4m9Q, TPZRq4FALB, 9Cu8MRmhq2, cNmu0hZ4CL`

| requery | response | provider | same_args | searched anchors |
|---|---|---|---:|---|
| 1 | `gen-1779491207-Pj1r2rCUHAb1PFWU6cD4` | GMICloud / `e9b742d8-f524-4795-8d84-0d5815e9b73b` (status 200) | False | `bESxQeXTlo, ZxsKRuP0o8, MbtUctg3KW, ZaudLwn0Hm, Zzs3JwknAY, Y7jJN0VQ4y, 6hP9JcXpNk, gTsLBDMZrL, cJs4oE4m9Q, cNmu0hZ4CL, 9Cu8MRmhq2, TTrzgEZt9s` |

Calls:

```json
[
  {
    "name": "calibration_search",
    "arguments": {
      "queries": [
        {
          "query": "few-shot anomaly detection prototype reconstruction",
          "n": 4,
          "high_score": 3.5
        },
        {
          "query": "multimodal anomaly detection few-shot",
          "n": 4,
          "low_score": 3.5,
          "high_score": 7.5
        },
        {
          "query": "anomaly detection prototype optimal transport",
          "n": 4,
          "low_score": 7.5
        }
      ]
    },
    "call_id": "call_826825787bd4497298d61ae9",
    "id": "fc_tmp_ple7tejfwyk"
  }
]
```

| 2 | `gen-1779491233-FpdUodiphzmipOXuEJgS` | GMICloud / `e9b742d8-f524-4795-8d84-0d5815e9b73b` (status 200) | False | `NO calibration_search` |

Calls:

```json
[
  {
    "name": "grep_paper",
    "arguments": {
      "paper_id": "7L7kmHHfgf",
      "pattern": "BTF"
    },
    "call_id": "call_4859ec9f039345158eb50d34",
    "id": "fc_tmp_ipz8937gvw"
  }
]
```

| 3 | `gen-1779491248-erePOLcdo5eRKkaQe26V` | GMICloud / `e9b742d8-f524-4795-8d84-0d5815e9b73b` (status 200) | False | `NO calibration_search` |

Calls:

```json
[
  {
    "name": "read_paper",
    "arguments": {
      "paper_id": "7L7kmHHfgf"
    },
    "call_id": "call_b91b8918def344e2beb57df9",
    "id": "fc_tmp_uxsx9galtz"
  }
]
```

### Stage 2 record 17

Old args:

```json
{
  "queries": [
    {
      "query": "few-shot anomaly detection multimodal reconstruction prototype optimal transport",
      "high_score": 6.0,
      "low_score": 4.5,
      "n": 5
    },
    {
      "query": "multimodal anomaly detection RGB 3D few-shot SOTA",
      "high_score": 7.5,
      "low_score": 6.0,
      "n": 5
    }
  ]
}
```

Old trace anchors: `gTsLBDMZrL, J2we1sVd9m, 8TBGdH3t6a, 3P87ptzvTm, 3WB5hT27zf, Zzs3JwknAY, JDiER86r8v, buC4E91xZE, ybFRoGxZjs, ENv1CeTwxc`

Old args replayed now anchors: `gTsLBDMZrL, J2we1sVd9m, 8TBGdH3t6a, 3P87ptzvTm, 3WB5hT27zf, Zzs3JwknAY, JDiER86r8v, buC4E91xZE, ybFRoGxZjs, ENv1CeTwxc`

| requery | response | provider | same_args | searched anchors |
|---|---|---|---:|---|
| 1 | `gen-1779491253-ujqL00aDYZYw9Lungfmx` | GMICloud / `e9b742d8-f524-4795-8d84-0d5815e9b73b` (status 200) | False | `gTsLBDMZrL, J2we1sVd9m, 8TBGdH3t6a, JDiER86r8v, Zzs3JwknAY, buC4E91xZE` |

Calls:

```json
[
  {
    "name": "calibration_search",
    "arguments": {
      "queries": [
        {
          "query": "few-shot anomaly detection prototype reconstruction optimal transport",
          "low_score": 4.5,
          "high_score": 6.5,
          "n": 3
        },
        {
          "query": "multimodal anomaly detection RGB 3D few-shot",
          "low_score": 6.0,
          "high_score": 7.5,
          "n": 3
        }
      ]
    },
    "call_id": "call_325b9385d5404af0b58361ff",
    "id": "fc_tmp_eaexkwqcuq6"
  }
]
```

| 2 | `gen-1779491264-dXgUV7pT3IkwsIgv1JY5` | GMICloud / `e9b742d8-f524-4795-8d84-0d5815e9b73b` (status 200) | False | `NO calibration_search` |

Calls:

```json
[
  {
    "name": "read_anchor",
    "arguments": {
      "anchor_id": "Vi6p2TeujL"
    },
    "call_id": "call_a774c384d35c459db0a6dd46",
    "id": "fc_tmp_9t6lejkwamm"
  },
  {
    "name": "read_anchor",
    "arguments": {
      "anchor_id": "J2we1sVd9m"
    },
    "call_id": "call_c3f462f59b65441d898057fd",
    "id": "fc_tmp_fsq3agkfet"
  }
]
```

| 3 | `gen-1779491269-3ausFcXjOLKeDrrYbUUM` | GMICloud / `e9b742d8-f524-4795-8d84-0d5815e9b73b` (status 200) | False | `gTsLBDMZrL, J2we1sVd9m, 3P87ptzvTm, 3WB5hT27zf, Zzs3JwknAY, VoLDkQ6yR3, buC4E91xZE, GySIAKEwtZ` |

Calls:

```json
[
  {
    "name": "calibration_search",
    "arguments": {
      "queries": [
        {
          "query": "multimodal anomaly detection few-shot optimal transport",
          "high_score": 6.0,
          "low_score": 4.5,
          "n": 4
        },
        {
          "query": "prototype reconstruction anomaly detection few-shot",
          "high_score": 7.5,
          "low_score": 6.0,
          "n": 4
        }
      ]
    },
    "call_id": "call_bc80756efe3247f69a7916cb",
    "id": "fc_tmp_ly3o6j9gf4q"
  }
]
```

