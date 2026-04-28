# ESDMotion: End-to-end Motion Prediction Only with SD Maps

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Motion prediction is a crucial task in autonomous driving. Existing motion prediction models rely on high-definition (HD) maps to provide environmental context for agents. However, offline HD maps require extensive manual annotation, making them costly and unscalable. Online mapping-based methods still require HD map annotation to train the online mapping module, which is costly as well and may also suffer from the issue of out-of-distribution map elements.
In this work, we explore conducting motion prediction with standard-definition (SD) maps as substitution, which are more readily available and offer broader coverage. One crucial challenge is that SD maps have low resolution and poor alignment accuracy. Directly replacing HD maps with SD maps leads to a significant drop in performance. 
We introduce end-to-end learning and specially tailored modules for SD maps to solve the problems. Specifically, we propose ESDMotion, the first end-to-end motion prediction framework that uses SD maps without any HD map supervision. We integrate BEV features obtained from raw sensor data into existing motion prediction models, with tailored designs for anchor-based and anchor-free models respectively. We find that the coarse and misaligned SD maps bring challenges to feature fusion of anchor-free model and on anchor generation of anchor-based model. Thus, we design two novel modules named Enhanced Road Observation and Pseudo Lane Expansion to address these issues. Benefiting from the end-to-end structure and new modules, ESDMotion outperforms the state-of-the-art online mapping-based motion prediction methods by 13.4\% in motion prediction performance and narrows the performance gap between HD and SD maps by 73\%. We will open source our code and checkpoints.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes an end-to-end trajectory prediction approach based on SD-map, termed ESDMotion, and validates its effectiveness across two common trajectory prediction paradigms: anchor-based and anchor-free schemes. The core contributions include an Enhanced Road Observation strategy to facilitate interaction between agent and SD-map features, as well as a Pseudo Lane Expansion approach to address the insufficient sampling of goal points in anchor-based methods by broadening the sampling range. Experiments on the nuScenes dataset shows the performance improvements in trajectory prediction using SD-map, narrowing the gap with the strategies that rely on HD maps.

### Strengths
1.This paper is the first to propose and validate the use of SD-Map for end-to-end trajectory prediction tasks. It achieves performance that is comparable to, or even surpasses, approaches utilizing online predicted HD-map.
2.The proposed strategy effectively reduces the trajectory prediction performance gap between using SD-map and HD-map.

### Weaknesses
1.The Pseudo Lane Expansion strategy proposed is a relatively coarse goal point sampling approach, as the generated pseudo lanes may not align with the actual road structure, potentially resulting in out-of-bound instances and other inaccuracies. Specifically, the method expands a fixed number of parallel lines at uniform distances from existing SD map lanes. This approach does not account for variations in road curvature, lane width, or the presence of obstacles, which could lead to sampled goal points that are not actually reachable or that lie outside the drivable area. The lack of adaptability in the expansion strategy is a significant limitation.
2.In the experimental section, validation is lacking for the performance of replacing SD-map with online HD-map predictions from models such as MapTRV2, combined with the proposed strategies in this study. Including this experiment would greatly enhance the validity of the paper's findings. Without this comparison, it is difficult to assess the true benefit of using SD-maps over predicted HD-maps, especially considering the potential for errors in both types of map data. The paper should also explore the performance of the proposed method when using predicted SD-maps instead of ground truth SD-maps.

Limitations

Although HD-maps are not required, this study still relies on offline-generated SD-Map, which limits its applicability. Additionally, for anchor-based trajectory prediction approaches, the proposed strategy does not demonstrate a performance advantage over methods that utilize online-predicted maps, highlighting a limitation of this approach.

### Questions
What will the trajectory prediction performance be like if the online predicted SD-map is used as input instead of the offline SD-map?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents ESDMotion, an end-to-end motion prediction framework that uses only standard-definition (SD) maps for autonomous driving motion prediction to address the limitations of high-definition maps. It integrates BEV features from raw sensor data into existing motion prediction models and presents Enhanced Road Observation and Pseudo Lane Expansion to handle the challenges brought by SD maps. Experiments on the nuScenes dataset show competitive performance compared to online mapping-based methods and mitigate the performance gap between HD and SD maps.

### Strengths
1. This paper proposes an end-to-end motion prediction framework that relies solely on SD maps, addressing the scalability and cost issues associated with HD maps.
2. This paper introduces Enhanced Road Observation and Pseudo Lane Expansion to enhance feature fusion and anchor generation for SD maps, addressing the limitations of using SD maps in motion prediction.
3. The proposed ESDMotion obtains comparable or even better performance compared to methods based on HD maps or GT maps.

### Weaknesses
1. Although the proposed approach ESDMotion obtains improvements in Tab.1&2, the baseline methods (DenseTNT and HiVT) are too old. It will be better to adopt the latest methods. Specifically, the field has seen rapid advancements, and using older baselines makes it difficult to assess the true impact of the proposed method against the current state-of-the-art. The performance gains might appear more significant than they actually are when compared to more recent, higher-performing models.
2. The proposed ESDMotion aims for end-to-end motion prediction however it still relies on SD maps as extra inputs, which is different from previous end-to-end works[1,2]. This reliance on SD maps, even if readily available, deviates from the pure end-to-end paradigm where the system learns directly from raw sensor data to motion predictions, without relying on intermediate map representations. This raises questions about the 'end-to-end' claim and the practical applicability of the method in scenarios where such maps might not be available or accurate.
3. The use of SDMap feature fusion as a way to enhance BEV features is already common; the authors focus on fusing BEV features and SDMap prior features around the agent, which is innovative but lacks sufficient novelty. While the focus on the agent's surrounding area is a practical choice, the core idea of fusing map and BEV features is not new, and the specific implementation details need to be more thoroughly justified to demonstrate a significant advancement over existing techniques. The novelty is incremental rather than groundbreaking.
4. The nuScenes dataset mostly contains simple road structure scenarios (PARA-Drive, BEVPlanner), in some complex scenarios, will the ESDMotion scheme proposed by the authors perform more excellently, for example, compared with PARA-Drive? The evaluation on nuScenes, while standard, might not fully reveal the limitations of the proposed method in more challenging and complex urban environments. The performance in simple scenarios might not translate well to more complex ones, and the paper lacks a discussion on the potential limitations of the approach in such situations.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To address the dependency of trajectory prediction models on high-cost offline high-precision maps or online mapping modules, this paper proposes ESDMotion. ESDMotion uses surround-view images and globally covered SD maps as environmental input for trajectory prediction, and experiments were conducted on nuScenes. The method proposed in this paper to use SDMap is interesting. However, I have concerns about the contributions of this paper and the fairness of some experiments.

### Strengths
1.Direct and clear motivation with coherent writing.  
2.The approaches of better utilizing SDMap (Pseudo Lane Expansion and Enhanced Road Observation) are interesting.

### Weaknesses
1.The paper is misleading (including the title and contribution 1) readers. It does not only rely on SD Map for trajectory prediction but rather combines surround-view images. The surround-view images provide crucial local environmental information, which models like HiVT and DenseTNT do not utilize.  
2.The emphasis on the end-to-end architecture of ESDMotion as a contribution is questionable. With BEVPred and ViP3D's work[1-2] and open-source code as a foundation, training a model end-to-end from images to BEV features to trajectory prediction presents no real challenges or contributions. The contribution of this paper seems lacking. Although the code[3] provided by BEVPred replaces mapping module features with HD maps as input for trajectory prediction, it can easily be modified to enable end-to-end training of the BEV encoder and trajectory prediction model.  
3.From Table 2, it can be seen that for HiVT, the minADE and minFDE using HDMap and SDMap are quite similar. While ESDMotion claims to improve minADE and minFDE through an end-to-end architecture or BEV features, as I mentioned in point 2, I believe this end-to-end architecture should not be counted as a contribution of this paper. This improvement can also be observed in the comparison between BEVPred and offline HDMap in Table 1.

### Questions
1.Although SD maps are globally covered, there are small areas like parking lots (which indeed exist in nuScenes) that are not covered. How does DenseTNT handle such situations?  
2.Why is ESDMotion unable to outperform BEVPred on DenseTNT?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a method to integrate Standard Definition (SD)-maps information in trajectory prediction models. The model jointly integrates sensor-based features (BEV maps) with SD-maps features with a deformable attention. Additionally, to account from the poor spatial localization of SD-maps, and missing fine-grained details, the method suggests a simple “pseudo-lane expansion” where artificial lanes are created parallelly to the main lane of the SD map. Each of these lanes serves in the deformable attention (“Enhanced Road Observation”) and provides goal candidates in anchor-based methods. Experiments are conducted on nuScenes.

### Strengths
* Introducing SD-maps, that are readily available with cheap and crowd-sourced maintenance, in trajectory prediction models is a good idea. While some previous works exist to use SD maps as priors to build HD maps, the impact on downstream application (here trajectory prediction) is an underexplored and important topic.

* The proposed modules are motivated, and their instantiation is sound.

* The method is designed for both anchor-based and anchor-free methods.

* The paper is well illustrated.

* The discussion on the contribution differences between SD / HD maps in anchor-based/anchor-free models was appreciated.

### Weaknesses
[Model presentation] The presentation of the method (section 3) could be significantly improved. In the current form, the model presentation interleaves the general trajectory prediction framework (from previous works), contributions of the work (enhanced road observation, pseudo lane expansion), high-level insights, and technical details (e.g. instantiation of the encoders, etc…). The presentation of the instantiation of the method for either anchor-based or anchor-free models can be also improved. For instance, the title of Section 3.2 targets anchor-free models but “the anchor-based model DenseTNT” is discussed at the end.

[Pseudo-lane expansion] DenseTNT already “expands” the lanes by densely sampling candidate goals around the lanes. It looks like the proposed pseudo-lane expansion simply amounts to increasing the size of the sampling kernel in denseTNT. Can the authors comment on this?

[Prior works] There are prior works that try to infer HD online maps from SD-maps and sensor-data [1,2,3] The reviewer suggests discussing these approaches in the related work section, as it offers another way to integrate SD maps.

* [1] Mind the map! Accounting for existing maps when estimating online HDMaps from sensors. Sun et al. 2023
* [2] Driving with Prior Maps: Unified Vector Prior Encoding for Autonomous Vehicle Mapping, Zeng et al. 2024
* [3] Local map Construction Methods with SD map: A Novel Survey, Li et al. 2024

[Fair baselines] The comparison between ESDMotion and “Unc”/”BEVPred” is unfair as ESDMotion uses SD maps which the latter ones do not (lines 369-374). Related to the previous remark, it would be valuable to compare ESDMotion with “Unc” + “online HD mapping based on SD maps” and “BEVPred” + “online HD mapping based on SD maps”.

[Impact of the Enhanced Road Observation] The improvement brought by the Enhanced Road Observation module is somewhat limited (Table 4).

[Map updates] The review agrees that HD maps must be often updated (l.43). However, I believe the use of SD maps does not solve this problem as SD maps should be updated as well.

[Multimodal future prediction] How many modes are generated by the models? (l.362,363).

[Title] The use of the word “only” in the title is questionable. There are some works doing end-to-end motion prediction without any maps (SD / HD).

[Writing clarity] The many paper typos, syntax and grammar issues hurt the readability of the paper. A thorough proof-read is strongly recommended. A non-exhaustive list of typos are shown below.
* “ground truth” → Hyphen is needed when used as an adjective
* Multiple spaces “ “ are missing, e.g., before citations, parenthesis, after “.” etc…
* Line 220. Is it Sec 4.3?
* Line 334. The subject is missing. “We”?
* Line 413 “tab1”
* Line 296 “an”
* Please refer to Figure 1 and Figure 6 in the text where appropriate.
* Figure 3 is discussed after Figure 4.
* Some notations are introduced but never used (e.g., l.293,335) 
* Opening double quote signs are off
* Illustrations are pixelated, pdf figures are generally preferred as they also allow for text selection and search.
* Tab 3 and 4 should be at the top of the page.
* In the reviewer’s opinion, the usage of bold sentences is too excessive.

### Questions
Beyond the need for improved paper presentation and proofreading, answers to the points on `[Pseudo-lane expansion]` and `[Fair baselines]` may lead to a reconsideration of the reviewer’s recommendation.

### Soundness
2

### Presentation
2

### Contribution
2
