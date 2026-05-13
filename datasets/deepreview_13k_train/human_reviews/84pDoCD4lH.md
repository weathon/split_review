# Do Vision-Language Models Represent Space and How? Evaluating Spatial Frame of Reference under Ambiguities

- Decision: Accept
- Scores: 10, 8, 8, 6, 5

## Abstract
\vspace*{-5pt}
Spatial expressions in situated communication can be ambiguous, as their meanings vary depending on the frames of reference (FoR) adopted by speakers and listeners. 
While spatial language understanding and reasoning by vision-language models (VLMs) have gained increasing attention, potential ambiguities in these models are still under-explored.
To address this issue, we present the \underline{CO}nsistent \underline{M}ultilingual \underline{F}rame \underline{O}f \underline{R}eference \underline{T}est (\dataset), an evaluation protocol to systematically assess the spatial reasoning capabilities of VLMs.
We evaluate nine state-of-the-art VLMs using \dataset.
Despite showing some alignment with English conventions in resolving ambiguities, our experiments reveal significant shortcomings of VLMs: notably, the models (1) exhibit poor robustness and consistency, (2) lack the flexibility to accommodate multiple FoRs, and (3) fail to adhere to language-specific or culture-specific conventions in cross-lingual tests, as English tends to dominate other languages. 
With a growing effort to align vision-language models with human cognitive intuitions, we call for more attention to the ambiguous nature and cross-cultural diversity of spatial reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors assess how VLMs represent space through the lens of “situated communication,” framing the meaning of spatial relations like “to the right of” under transformations, in different frames of reference, and others (situated communication).

They introduce the COMFORT dataset, tasks, and metrics to analyze spatial reasoning under these classes of transformations, and see which frame-of-reference preferences LMs have, and test whether these preferences are language-agnostic by extending their evaluation to multilingual settings. 

The images are rendered to enable simple dynamic generation of test samples. Their language queries that test the relations likewise have a simple structure and are programmatically produced, enabling translation into other languages. Testing the kinds of relations is simple using this methodology and allows them to test for continua such as how a model rates the “in front of” relation by angle between the two in the plane relative to the camera.

**Edit**: The authors did a great job adding some small case studies that **show** how their results generalize to other backgrounds and real images (although these are still pretty close to in-distribution to the test images). The use of a laptop rather than a ball in the real images in particular is a strong change. I have raised all the component scores to 4. **Although I would prefer an option to give a 9/10, since it isn't available I will raise from 8 to 10.**

These tests are then translated into metrics using the established concept of “acceptability regions”, which then allows them to score for correctness. Swapping object types, colors, etc in the same scene is easy using the synthetic pipeline and gives an evaluable sense of robustness.

They test a broad set of VLMs, including multilingual ones in 109 translated languages. Some models better represent egocentric vs object centric relations.

Overall, they find that the VLMs do have some acceptable egocentric understanding capabilities but they have severe robustness issues. They find that English notions of frame of reference are held across most test languages, not reflecting the diversity of notions.

### Strengths
Deep utilization of synthetic pipeline to really probe spatial perception from several angles.

Demonstrations of anglewise judgements are compelling and surprising! (eg., figure 7)

Great to see the extra effort of testing 

Conclusions and discussion are thoughtful and well supported.

### Weaknesses
 ~Sole reliance on synthetic data.~ A brief ablation over natural images would be nice to see to give a sense of how well these findings generalize. They added the case study, the results generalize (though the case study is still close to ID the synth data)!

~Limited diversity of backgrounds. This is another form of variation that may have important implications for generalization.~ They added the case study, the findings generalize!

The multilingual experiments, while welcome, have limited time to breathe in the overall paper with just a few paragraphs and tables stuck in appendices. However, I think this is a great problem to have as the paper is densely packed with quality experimentation.

### Questions
Small grammar errors, eg 476: “Does multilingual VLMs..” -> “Do multilingual…” Maybe do a brief grammarly check?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
**Main contributions**: 
The paper has two main contributions: 
1. It presents COMFORT, a framework for evaluating VLMs' understanding of spatial frame of reference expressions, which relate two objects to one another (e.g. "Is the basketball *to the right of* the car?"). Expressions are evaluated using a rendered image containing the two objects and which is used to query the VLM with (as a binary Yes/No question) for whether or not the relation holds for the image. 

2. It uses COMFORT to show that a set of contemporary VLMs have distinct preferences for frame of reference parameters. Specifically, the paper presents evidence for the preference of English language frame of reference parameters in VLMs. 

**Framework Structure**:  
Expressions in COMFORT vary across two main conditions:
1. Expressions which include two objects with a semantic "front" (e.g. such as the "front" of a person being the side with the person's face). In this scenario the spatial expression must be reasoned about in terms of an anchor frame of reference (i.e. either object A's, object B's, or the camera's frame). The selection of the frame of reference will determine which direction in the image corresponds to "left of", "back of" etc. 

2. Expressions which include objects without a semantic "front". In COMFORT, this is instantiated by scenarios with two balls. In such scenarios, a coordinate transformation convention must be assumed for determining what is "right", "left", "back", etc. Different languages have different standard conventions, and so this condition is set up to test this. 

Preferences are measured by evaluating the [Yes/No] probability for a given spatial expression in relation to a ground truth *region of acceptability*, a continuous region of rotation of the second object around the center object (see Figure 1c for reference) in which a spatial expression may hold true. This region of acceptability allows for not only for accuracy to be measured but also for the dynamics of the probability to be measured as functions of distance from the center of the region of acceptability -- intuitively, the score of "right of" should decrease smoothly as the object is rotated from 0 to 90 degrees from the center of the region. Specifically, the paper presents. 
These measures probe the robustness of model scores (e.g. evaluating std across object variations unrelated to space like color or shape) as well as the consistency (are scores symmetric at both equivalent angles from the acceptability region's center? Do they change smoothly as angle is varied?). 

**Results**
The paper uses the region of acceptability based error measures to show that VLMs generally skew towards preferring egocentric frames of references (condition 1) and the reflected coordinate transformation convention. Additionally, the paper also shows that these preferences cannot be reliably changed when the prompt explicitly defines the frame of reference to be used, or when a language (other than English) with different known preferences is used to prompt the model.

**Recommendation** 
This is a solid paper which I believe presents a unique contribution that stands to better capacitate the community in vetting the spatial understanding of VLMs. I have noted a few suggestions below under Weaknesses to improve the presentation of the paper. With that said, I think it is already at a good quality and I recommend acceptance.

### Strengths
**Strong Backing in Theory**: The paper's framing and setup in sections 1 through 3 (which motivates the problem statement and framework design choices) is a joy to read. Motivating statements and scoping within existing work is very clear and compelling. 

**Conclusions Well Supported**: The experimental setup is quite thorough and shows clear trends which the authors use to justify their claims. A majority of models are clearly shown to have FoR preferences based on the metrics *cos* and *hem* error functions defined, with the BLIP family of VLMs being a notable exception. I particularly appreciated that the paper additionally presents a compelling explanation for the BLIP discrepancy by showing that these same models score poorly on an evaluation of object hallucinations. 

**Novelty**: In my understanding I believe that the presented framework is novel based on its continuous definition based on regions of acceptability. This seems to me to be an important distinction namely because these spatial relationships are known to lie within continuums and are not discrete. 

**Clarity**: The paper's writing is generally clear, and I found the organizational structure helpful for understanding the concepts introduced.

### Weaknesses
 **Cross-lingual Experiment Presentation**: I think some further refinement/elaboration of the cross lingual experiments (Section 4.5) could help strengthen the paper. Although the paper does state upfront that it spends most of the content focused around English experiments, the treatment of the section still felt a little too short for the emphasis that is placed in the introduction for this being a core piece of the framework (e.g. the M in COMFORT stands for Multilingual). Specifically I think a couple of details could be expanded upon.

First, the results in Figure 8 are a little ambiguously presented. Is the world map mapping the preferences of GPT-4o, or is it mapping ground truth human preferences? I believe the former, but the wording in both the figure and the paper makes it sound like these are ground truth preferences. 
Second, for ground truth preferences, I'm wondering how these are obtained? -- I'm assuming this is pulled from the linguistics literature, but it is not explicitly stated and appears like a key detail to me. I would appreciate it if the authors could clarify both of these points. 

Lastly, although the results presented clearly show a preference for the same reference frames as English, I think they could be strengthened by also showing a notion of what the expected preferences would be if the VLM were to be adhering to the conventions of the language being used. For example, I think this could be done by (a) adding a second map showing a visualization of ground truth human preferences, or (b) adding the bold/underline convention from the table in Figure 8 to Table 10.

### Questions
**Suggestions**: 
* L212 "the query is appended after four different perspective prompts...": I'm assuming this meant to say "after *one of* four different..."? 

* I understand the authors may have been space limited (no pun intended), but I think adding a Conclusion section to reiterate contributions and takeaways (further than the Discussion section already does) could make the paper stronger. There's a large amount of content, so spoon-feeding the final takeaways to readers could aid clarity. 

* This is minor, but relatedly I think the paper could be a little clearer about what the intended usage of the framework is for readers. Are readers supposed to come away with an understanding that this will be a benchmark they can evaluate their own models on? I believe yes, but the wording of the paper at the beginning and end doesn't make this explicit. In the introduction, COMFORT is introduced as a "framework" and not a "benchmark", was this intentional? Secondly, the paper closes with only a discussion over the empirical findings in Section 5, without any explicit reiteration that it has introduced COMFORT. This omission at the end made it feel like the only point of the paper was to present a study of VLM spatial understanding -- this would be fine of course, but if I'm understanding correctly I think the paper would additionally want to explicitly market itself as offering COMFORT as a testbed for VLMs. It's subtle, but I think being explicit about this, especially at the end of the paper, could really help drive home the point the authors want to communicate.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper explores the spatial reasoning capabilities of vision-language models (VLMs) and their handling of spatial ambiguities. It introduces the COnsistent Multilingual Frame Of Reference Test (COMFORT) to systematically evaluate these models. The study reveals that while VLMs show some alignment with English conventions in resolving spatial ambiguities, they exhibit significant shortcomings: poor robustness and consistency, lack of flexibility to accommodate multiple frames of reference (FoRs), and failure to adhere to language-specific or culture-specific conventions in cross-lingual tests. The paper emphasizes the need for more attention to the ambiguous nature and cross-cultural diversity of spatial reasoning in VLMs.

### Strengths
This paper introduces the innovative COnsistent Multilingual Frame Of Reference Test (COMFORT), which systematically evaluates vision-language models (VLMs) across multiple languages and cultural contexts. This novel approach highlights the importance of considering linguistic and cultural variations in model performance. The research is thorough and methodical, assessing nine state-of-the-art VLMs with detailed analyses of their robustness, consistency, and flexibility. The paper is well-organized and clearly written, making complex concepts accessible. Its findings underscore the need for more robust and flexible models, providing a valuable framework for future research in vision-language modeling and spatial reasoning.

### Weaknesses
The scope of spatial relations is limited, focusing mainly on basic relations like front-back and left-right, while neglecting others such as near-far and above-below. This narrow focus restricts the evaluation to a small subset of spatial reasoning, failing to address the complexity of spatial understanding in real-world scenarios. The evaluation relies on synthetic 3D images, which may not fully capture real-world complexities, and lacks consideration for occlusion and varying camera angles. The use of synthetic data, while offering control, introduces a domain gap that could limit the generalizability of the findings to real-world images with diverse lighting, textures, and object variations. Additionally, the analysis could benefit from a more diverse linguistic and cultural context, as well as human annotations for the multilingual dataset. The current analysis does not fully explore the nuances of spatial language across different cultures, and the lack of human annotations raises concerns about the accuracy and reliability of the evaluation, especially in multilingual settings where subtle differences in spatial language can be crucial.

### Questions
1. How do the findings impact the development of embodied AI systems and other applications like autonomous driving, robotics, or augmented reality?

2. How could improved spatial reasoning in vision-language models (VLMs) enhance performance in multilingual and multicultural contexts?

3. What are the key areas of future research to advance the spatial reasoning capabilities of VLMs, and what specific challenges or limitations need to be addressed?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper discusses the performance of VLMs in handling ambiguity in spatial expressions. The authors constructed a new benchmark -COMFORT to systematically test the spatial reasoning capabilities of VLMs, and conducted analysis on COMFORT.

### Strengths
1. This paper delves into "Do VLM represent space and how". Specifically, it considers the concept of Frames of Reference (FoR) and constructs a framework for understanding how VLMs perceive spatial information, taking into account the ambiguities that FoR might bring. The COMFORT framework is systematic and comprehensive, and its task formulation is rigorous. The authors create challenging but realistic queries using synthetic 3D images and corresponding textual descriptions, and propose systematic metrics. From the perspective of benchmark construction, this is a systematic and rigorous work.

2. The authors tested different VLMs and analyzed how they internally understand spatial representations. The testing methods are reliable.

3. The authors extended the test cases to cover 109 languages across 170 regions, further testing how VLMs respond to ambiguities in spatial relationship descriptions under different languages.

### Weaknesses
As the author claimed, "spatial expressions in situated communication can be ambiguous." Therefore, considering that humans also exhibit different understandings when dealing with similar issues of ambiguity, even if VLMs demonstrate different interpretations, it does not necessarily imply a clear superiority or inferiority. In other words, the evaluation metrics proposed in the paper are not absolute criteria, like egocentric is not naturally better than addressee-centered, but rather serve as perspectives for observing how VLMs understand spatial information. 

From this standpoint, I believe the author should include more analysis of how humans understand ambiguities in spatial relations (relevant information can be found in psychological and cognitive science research). This would help us better understand the differences between VLMs’ understanding of these ambiguities and the human perspective, and ultimately facilitate a better alignment of spatial reasoning in vision-language models with human cognition.

Hope to see further discussion on these points.

### Questions
Please refer to the comments in the Weakness.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
- Investigates how vision-language models (VLMs) represent and reason about spatial relations, particularly when spatial language is ambiguous due to differing frames of reference (FoRs). It focuses on evaluating the robustness, consistency, and flexibility of VLMs in handling such ambiguities.

- The authors introduce a new evaluation protocol called the COnsistent Multilingual Frame Of Reference Test (COMFORT), which systematically assesses VLMs' spatial reasoning capabilities. The evaluation includes tasks with synthetic 3D images and text descriptions of spatial relations, with tests conducted in 109 languages across 170 regions worldwide.

- The study reveals that while VLMs show some alignment with English conventions for resolving spatial ambiguities, they struggle with: (A) Consistency and robustness in spatial reasoning, (B) Flexibility in adopting multiple FoRs, (C) Cross-linguistic and cross-cultural understanding of spatial relations, with English conventions often dominating over those of other languages.

### Strengths
- Unlike existing benchmarks, which typically focus on spatial language understanding within a single frame of reference or specific cultural context, this work broadens the scope by emphasizing ambiguity in spatial reasoning due to different Framework of References and cross-linguistic/cross-cultural diversity.

- The paper is well-structured, with clear explanations of key concepts such as frames of reference and spatial reasoning.

More importantly, 

- The paper’s contributions are highly significant in the context of both vision-language research and broader discussions on AI alignment with human cognition. By focusing on spatial reasoning, a core component of human cognition, this work addresses a critical gap in the evaluation of VLMs.

- The cross-lingual evaluation across diverse cultural backgrounds provides valuable insights into the limitations of current VLMs in handling non-English spatial conventions. This has implications for the development of more globally applicable models, as the dominance of English-centric FoRs could hinder the usability of VLMs in non-English contexts.

### Weaknesses
 - While the introduction of the COMFORT benchmark is a novel contribution, the idea of testing spatial reasoning in vision-language models is not entirely new. Several previous benchmarks, such as those mentioned in the paper, have evaluated spatial reasoning capabilities in VLMs. The novelty of this paper lies primarily in its focus on the frame of reference ambiguities, but the paper does not sufficiently clarify how this focus significantly advances beyond the existing benchmarks. But I agree that the frame of reference is a rather novel take on the same topic.

- Although the paper provides valuable insights into how English conventions dominate spatial reasoning in multilingual models, the discussion around cultural and linguistic biases remains relatively high-level. The paper identifies that most models tend to default to egocentric relative frames of reference, which aligns with English spatial conventions. However, it does not deeply investigate whether this bias toward egocentrism is inherently problematic across all contexts or if there are scenarios where this behavior is acceptable or even preferable. 

+ (not required) It would be beneficial to include a dedicated section discussing the practical relevance of the findings in LLM applications. Is there an area the the findings of this paper can seriously affect?

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3
