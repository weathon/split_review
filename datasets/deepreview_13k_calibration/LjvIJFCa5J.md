# CityNav: Language-Goal Aerial Navigation Dataset Using Geographic Information

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
Vision-and-language navigation (VLN) aims to guide autonomous agents through real-world environments by integrating visual and linguistic cues.
Despite notable advancements in ground-level navigation, the exploration of aerial navigation using these modalities remains limited. 
This gap primarily arises from a lack of suitable resources for real-world, city-scale aerial navigation studies.
To remedy this gap, we introduce CityNav, a novel dataset explicitly designed for language-guided aerial navigation in photorealistic 3D environments of real cities.
CityNav comprises 32k natural language descriptions paired with human demonstration trajectories, collected via a newly developed web-based 3D simulator.
Each description identifies a navigation goal, utilizing the names and locations of landmarks within actual cities.
As an initial step toward addressing this challenge, we provide baseline models of navigation agents that incorporate an internal 2D spatial map representing landmarks referenced in the descriptions.
We have benchmarked the latest aerial navigation methods alongside our proposed baseline model on the CityNav dataset.
The findings are revealing: (i) our aerial agent model trained on human demonstration trajectories,  outperform those trained on shortest path trajectories by a large margin;
(ii) incorporating 2D spatial map information markedly and robustly enhances navigation performance at a city scale; 
(iii) despite the use of map information, our challenging CityNav dataset reveals a persistent performance gap between our baseline models and human performance.
To foster further research in aerial VLN, we have made the dataset and code available at 
https://water-cookie.io/city-nav-proj/

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The manuscript introduces CityNav, a comprehensive dataset designed for language-guided aerial navigation using real-world 3D urban environments. This dataset addresses a notable gap in the field by enabling aerial vision-and-language navigation (VLN) research with realistic data. CityNav includes over 32,000 natural language descriptions paired with human demonstration trajectories, collected through a novel web-based 3D flight simulator. The paper presents benchmark results for navigation models, highlighting significant performance enhancements through the use of a map-based goal prediction model.

### Strengths
1. The introduction of CityNav fills an important void in aerial VLN research, offering a large-scale, realistic dataset with geo-referenced human trajectories.

2. The dataset's scale and the use of actual 3D scans of urban areas significantly improve realism compared to synthetic or satellite-only data.

### Weaknesses
1. The current dataset lacks dynamic elements and agent-object interactions, such as moving vehicles, pedestrian, the varying light, etc., reducing applicability to real-world, complex urban settings.

2. The generation of the dataset seems very engineering and laborious, where the instructions and trajectories are obtained by MTurk. The dataset is mostly based on existing city-scale point cloud data from SensatUrban. Actually, SensatUrban just contain the images from some view of the field and sparse point clouds, while not images from each view as NeRF and Gaussian Splatting. In this case, view rendering works should be done to make the dataset more applicable. Besides, I wonder the gap between the simulation and real flight.

3. This work just implement a simple baseline, which lacks novelty and insight about the special challenges in this field. In my view, the object on the street is structural, such as road, cars, pedestrains, etc, and these objects are very small. During flight, the geographical objects are captured from differnet views and distance, which increase the difficulty to recognition. In this case,  more specific and innovative method should be proposed.

### Questions
please address my concerns in the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces CityNav, a new 3D simulator and dataset for language-guided aerial navigation, filling the resource gap in city-scale aerial navigation. The dataset includes 32,000 descriptions paired with human trajectories and proposes a baseline model using spatial maps. However, high-altitude operations may impact the detection of small objects, and the lack of environmental interaction raises concerns about realism. Moreover, more balanced evaluation and clearer experimental setups are needed.

### Strengths
1. CityNav introduced a new web-based 3D simulator designed to collect and test language-guided aerial navigation tasks.
2. The CityNav dataset includes 32,000 natural language descriptions paired with human demonstration trajectories. This dataset fills the resource gap in the aerial navigation domain, providing valuable resources for city-scale aerial navigation research.
3. By incorporating spatial map information, the baseline model provides a foundation for future city-scale aerial navigation tasks, exploring how to effectively utilize linguistic and visual cues for navigation.

### Weaknesses
1. The prevalence of forward and down actions suggests that the drone operates at relatively high altitudes, which may hinder object recognition and make it challenging to observe smaller objects, such as vehicles. 
2. The paper mentions a lack of interaction with environmental objects during navigation, indicating that the model may do not account for realistic challenges like collision. 
3. The use of the landmark map as an additional prior for the MGP model raises concerns about fairness in evaluation. This additional information might skew the comparison with models that do not utilize such priors.  
4. Several experimental concerns are raised in the study, which will be detailed in the questions.

### Questions
1. The majority of annotated actions are forward and down. When the drone is at a high altitude, does the annotated data make it difficult to detect small objects like vehicles?
2. Were collisions with environmental objects considered during data collection and model evaluation, particularly in the shortest path annotations?
3. Why do Seq2Seq and CMA models perform better under the SP setting compared to the HD setting in Table 2?
4. Why is the Navigation Error (NE) difference between different difficulty levels in Table 3 so small?
4. Does the landmark map give the MGP model an unfair advantage during evaluation? Would introducing similar priors to other models create a more balanced comparison?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces CityNav, a dataset designed for language-guided aerial navigation in real-world, photorealistic 3D city environments. CityNav encompasses over 32k natural language descriptions paired with human-generated trajectories. The dataset leverages 3D scans of actual cities, incorporating a web-based 3D flight simulator that syncs with world maps for trajectory collection. This dataset provides a diverse set of realistic trajectories and linguistic descriptions. Through their analysis, the authors reveal that models trained with human demonstrations substantially outperform those relying on shortest path trajectories, and the integration of 2D spatial maps markedly enhances navigation performance. However, there remains a significant performance gap between automated models and human navigators.

### Strengths
1. The paper introduces CityNav, a new dataset for outdoor aerial vision-and-language navigation in real-world urban settings.
2. The dataset includes high-quality data with detailed annotations.
3. The authors provide access to the dataset and the code, enhancing reproducibility and facilitating further research.

### Weaknesses
1. The analysis of the experiments is not entirely convincing, as the discussion in the paper lacks explanations for the underlying reasons of the observed performance. This insufficiency makes it challenging to fully assess the effectiveness of the proposed dataset and benchmark. Specifically, the paper does not adequately explore why human demonstrations outperform shortest-path trajectories, beyond stating that human paths are more effective. The analysis should delve into the specific characteristics of human trajectories, such as the frequency of landmark visits, the distribution of actions around landmarks, and the overall path diversity, to provide a more thorough understanding of the performance differences.
2. The authors do not adequately explain the practical value of the Aerial VLN task that the CityNav dataset is designed to support. Without a clear connection between the Aerial VLN and its potential applications, the significance of the proposed dataset remains unclear. The paper fails to justify why language-guided navigation is necessary when GPS and map data are readily available. The scenarios presented, such as disaster relief, do not convincingly demonstrate the need for language-based navigation over traditional positioning systems. The paper should provide a more compelling argument for the unique advantages of Aerial VLN in real-world applications, especially when compared to existing, more reliable methods.

### Questions
1. Could the authors provide a more detailed analysis of the differences between human and shortest-path trajectories? In the abstract, the authors mention that "human demonstration trajectories outperform those trained on shortest path trajectories by a large margin." I am curious about the reasons behind the superior performance of human demonstrations. Specifically, do human demonstrations provide more information within the trajectory compared to shortest paths, which might only have start and end points? If this is the case, the comparison lacks persuasiveness because the information provided by human demonstrations is much denser and more extensive than that of the shortest path. 
2. The authors do not provide a convincing explanation of the value of the Aerial VLN task when introducing it. From an academic perspective, what distinguishes Aerial VLN from other Indoor VLN tasks that warrant attention? Could the authors please provide a more detailed comparison between Aerial VLN and Indoor VLN, highlighting specific challenges or opportunities unique to the aerial domain? 
3. Meanwhile, could the authors please discuss real-world scenarios where language guidance might offer advantages over GPS, perhaps drawing on existing literature or use cases? Specifically, why opt for language guidance over traditional positioning systems like GPS, especially when maps are available? 
4. Furthermore, I am confused about the experiments in disaster scenarios. The additional experiments mentioned in the appendix, which assume the failure of GPS systems during major natural disasters, further raise concerns about the practical application of this task. It is questionable whether GPS systems would indeed be significantly disrupted by such events (±100m). Moreover, the simulation assumes that the map-based VLN system remains stable under such conditions. What evidence supports these disaster scenario simulations, and do they reflect realistic conditions, or do they indicate a lack of real-world applicability for the task? Could the authors please provide evidence or citations supporting the GPS disruption levels used in their disaster scenarios, and explain how their VLN system's stability was modeled in these conditions?

If the authors are willing to address my questions, I would be very pleased to continue this discussion with them.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a novel dataset for aerial VLN (vision-language-navigation) called CityNav. It consists of about 32k pairs, where the first entry = natural language description of goal, and second entry = human demonstration of reaching the goal. The latter is collected using Mechanical Turk in a newly developed web-based 3D simulator. The dataset depicts photorealistic urban scenes. In addition to the dataset, several learning-based baseline methods are evaluated (and one is specifically developed within the paper), to provide a suite of baseline results against which future researchers can compare. The various methods are evaluated in two settings: (i) imitation learning based on shortest path trajectories; (ii) same but based on human trajectories. It is shown that results in general get better in the setting (ii).

### Strengths
* The main and strongest contribution is (quite naturally) the dataset itself, CityNav. It is a factor 4x or so larger than the 2nd largest similar dataset, and with intriguing advantages relative to recent similar works:
    - Based on real-world point clouds (although this work is based on SensatUrban from 2022, so it is intself not a contribution).
    - Takes into account realistic challenges related to 3D geometries in real UAV missions.

* Many relevant experiments to showcase the strength of the proposed dataset are included, e.g.
    - Several imitation learning-based baselines are evaluated / developed, to give a strong suite of baseline results against which future work can be compared.
    - Great to see the various results with methods trained based on either shortest path or human demonstrations, which showed human demonstrations lead to better results overall.
    - Several relevant "additional results", including proper ablations of the proposed MGP method, examination into the effect of training size (interesting to see that the size is more important when training based on human trajectories vs when trained on shortest path), evaluations on different difficulty levels, and some results on challening conditions such as gnss-disturbed environments.
    - Good that several relevant and widely used metrics were used.

* I think the stuff written around Line 311 on "Quality control" was good and made it feel like the dataset was carefully designed. For example, the rigorous selection of which human trajectories were kept in the dataset, etc. Also, speaking of the dataset, I liked the plots that showed some key characteristics about the data, e.g. Fig 4 e-f.

* The anonymous webpage had great visualizations which further helped me understand the task setup.

* Great that the code was accompanied with the submission, it further strengthens the validity of the work.

### Weaknesses
 * Some things were not quite clear to me regarding the use / not use of maps. So the proposed MGP method seems to use a map (but see questions below, I might have misunderstood), and so the the human annotators. Meanwhile, the other learning-based methods do not. I'm not quite sure I get the reasoning about why maps make sense to use as input, or in particular I dont see the realism behind it, e.g. if considering gnss-free settings. Now that said, it's fine IMO to have such results, but I found the "focus" on these map-based things to be a bit.. "off" relative to the applications I envision.

* Adding to the above, it'd be great to see the dataset accompanied by human trajectories that were collected by humans that dit NOT get to use maps. Perhaps training on such trajectories is beneficial especially for learning-based methods that do not have maps. (I understand that this is beyond the scope of addressing within this rebuttal, but still adding as a weakness for now.)

* I think some results on RL-based approaches would significantly improve the suite of learning-based baselines. Currently, only imitation learning-based methods are shown. In the RL case, some appropriate reward must of course be specified.

* To the best of my knowledge, no inference runtimes (e.g. time per action) were mentioned for the various methods, and I think it should be reported alongside the other metrics.

* I think the paper would be strengthened by explicitly showing results (both for learning-based methods and for the human trajectories) at category-level. For instance, it can provide insights about whether the class imbalance (that e.g. much more "Building" than "Parking lot") affects results in any way, e.g. if results get worse on "Parking lot" than "Building".

* Maybe I missed it but I didn't see the distribution geographically of which and how many cities / urban areas were included. This should be included in the paper.

* Misc (do not affect my rating):
    - I don't quite agree that the aerial VLN task is in general more challenging than ground VLN, necessarily as stated on Line 170 (since ground based counterparts have more challenging with occlusions etc). Please consider rephrasing a bit.
    - I think Fig 4 can be improved by mentioning what data splits are used in the various subfigures, e.g. if some only based on Train, if some based on overall union, etc.
    - I think that the shortest path "oracle method" can be reported below "Human" in Table 2, it's a nice upper-bound method to compare the rest with. Also, speaking of tables, I think it'd be great if the captions included what splits were used in tables such as Table 3 (e.g. Test unseen and so on -- i know this is mentioned in the main text, but still helpful).

### Questions
* Please try to address as many of the weaknesses as possible but I understand that time is a very limiting factor so here are some priorities:
    - Is there a particular reason why RL-based method(s) were not used, i.e. why only imitation learning?
    - What are runtimes per action / trajectory during inference?
    - Is the proposed MGP method using actual maps as input or are they somehow generated by the model? If the former, do you not agree that it may be unrealistic to provide such a map, e.g. in GNSS-free settings?
    - Did I miss it, or did you not include geographical distribution of the various cities / urban areas of the dataset? If not included, please add to cam-ready, and also please comment on the distribution here.

* I did not get this part in the box on Line 295: "Note that you cannot replace the marker." <-- It seems to me that this constraint leaves room for lots of mistakes that are unnecessary. Why not include an "undo" button..?

* The 170+ MTurk annotators, where were they distributed across the globe? Were the randomly selected?  Also, were exactly one person used as demonstrator per "game", or multi-annotator setup used?

* Why were the easy-medium-hard thingys mentioned as "-" on "Train" in Fig. 4a? Why could they not be listed?

### Soundness
3

### Presentation
3

### Contribution
4
