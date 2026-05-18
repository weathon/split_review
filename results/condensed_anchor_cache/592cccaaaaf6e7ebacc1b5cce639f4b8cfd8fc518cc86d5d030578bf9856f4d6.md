- Decision: Reject
- Scores: 3, 3, 3

## Merged Review

### Summary
The paper introduces SyGRID, a synthetic industrial object dataset generated using a physically-based renderer (PBR) on 10 distinct objects, considering various materials, lighting conditions, and background textures. It includes cluttered multi-object scenes with rigid-body physics and supports tasks: 2D detection, segmentation, depth estimation, and 6D pose estimation. Extensive experiments on simulated and real data assess realism and sim-to-real transfer.

### Strengths
- Well-written, clear, easy to follow; thorough literature review of prior industrial datasets presented visually via tables.
- Comprehensive experiments demonstrate the dataset is more realistic than prior synthetic datasets, about on par with YCBV, partially closing the sim-to-real gap.
- The target scenario (realistic industrial environment with clutter and transparency) is practical, not yet well studied, and needed for downstream robotic tasks; the dataset will contribute to the field (Reviewer 3).

### Weaknesses
- **Limited novelty**: The claimed novelties (cluttered scenes, varied lighting, diverse materials, reflective/transparent objects) are already well supported by modern PBR pipelines and prior work such as Omni6D. The paper does not clarify how its rendering techniques or material properties differ from existing PBR capabilities; specific details on algorithms for reflective/transparent materials are missing.
- **Very small dataset size (10 object instances)**: Industrial environments typically have many more object types and categories. The limited diversity risks being too specific to the initial use case and not generalizable. It is unclear whether diversity exists within categories or only across categories.
- **Viewpoint limitations**: Only top-down viewpoints are captured; oblique/side views are absent. The paper does not specify the range of camera distances used. This limits applicability to real-world scenarios with varying camera angles.
- **Insufficient motivation and practical justification**: The dataset is narrowly focused on a specific bin-picking task with a small object set; it is unclear what real industrial applications use these exact parts. Industrial settings are often highly controllable (lighting, structured object presentation), making emphasis on clutter/occlusions/questionable. The paper does not address this contrast or cite specific industrial applications.
- **Large remaining sim-to-real gap**: Table 2 shows a significant performance drop on real vs. synthetic test data (segmentation: -15% to –20%, depth: 10× error, rotation error: 2–6× larger). The paper provides no analysis of why the gap remains so large, nor whether it stems from limited synthetic diversity or real data quality.
- **Lack of out-of-distribution generalization tests**: No experiments evaluate models trained on SyGRID on other datasets (e.g., those in Table 1), novel object categories, or different clutter types.
- **No real-world robotic validation**: The stated goal is facilitating downstream robotic manipulation, yet the evaluation is confined to perception metrics in simulation. The paper should demonstrate sim-to-real transfer on physical robotic tasks with metrics such as grasping success rate. The real-world manipulation video would be more informative with policy visualizations instead of only raw execution footage.
- **Presentation**: Paragraphs are overly long and should be divided for readability (Reviewer 3).