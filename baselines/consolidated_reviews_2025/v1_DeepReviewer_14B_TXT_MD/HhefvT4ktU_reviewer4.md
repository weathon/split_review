### Summary

This paper investigates the extent to which the Stable Diffusion XL (SDXL) model, a widely used text-to-image generative AI, exhibits racial and gender stereotypes. The authors document significant biases in SDXL across six races, two genders, 32 professions, and eight attributes. They also examine the degree to which SDXL depicts individuals of the same race as being similar to one another, revealing racial homogenization. The paper proposes novel debiasing solutions, called SDXL-Inc and SDXL-Div, to address these stereotypes and homogenization. Finally, through a preregistered experiment, the authors demonstrate that exposure to inclusive AI-generated faces reduces people's racial and gender biases, while exposure to non-inclusive ones increases such biases. The findings emphasize the need to address biases and stereotypes in AI-generated content.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a critical and timely issue in the field of AI, specifically the presence of racial and gender stereotypes in widely used text-to-image models. Given the increasing use of such models in various applications, understanding and mitigating these biases is crucial for ensuring fairness and preventing the perpetuation of harmful stereotypes in AI-generated content.

2. The authors conduct a comprehensive analysis of biases in SDXL, examining its behavior across multiple dimensions, including race, gender, profession, and attributes. This thorough approach provides a detailed understanding of the types and extent of biases present in the model.

3. The paper proposes a debiasing solution, SDXL-Inc, and demonstrates its effectiveness in reducing biases in AI-generated images. The authors further strengthen their claims by conducting a preregistered experiment that shows the impact of exposure to inclusive AI-generated faces on people's own biases.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that "none of the studies proposed debiasing solutions." However, there are several relevant works, e.g., [1] and [2].
2. The proposed debiasing solution is to fine-tune SDXL using LoRA. Although this is an effective solution, it is not a novel method.
3. The user study only includes 135 participants. This is a relatively small number of participants. The authors should consider using a larger number of participants.
4. The authors only conduct user studies on American participants. It is unclear whether the conclusions can be applied to people from other countries.
5. The authors only conduct user studies on people whose first language is English. It is unclear whether the conclusions can be applied to people who speak other languages.
6. The authors only conduct user studies on people who are residents of the US. It is unclear whether the conclusions can be applied to people who are not residents of the US.
7. The authors only conduct user studies on people who are from 21 US states. It is unclear whether the conclusions can be applied to people who are from other US states.
8. The authors should also conduct user studies on SDXL-Inc without revealing that the images are generated using SDXL-Inc, and compare the results with the "labeled as AI-generated" results.
9. The authors should also conduct user studies on other models, e.g., ITI-GEN and Fair Diffusion, and compare the results with SDXL-Inc.

### Suggestions

The authors should significantly expand the scope of their user studies to address the limitations in the current experimental design. The limited geographic and linguistic scope of the participant pool raises serious concerns about the generalizability of the findings. The study should include participants from a more diverse range of countries, languages, and regions within those countries. For example, the authors could recruit participants from different continents, including Africa, Asia, and South America, to ensure that the results are not biased towards a Western perspective. Furthermore, the authors should consider including participants who speak languages other than English, such as Spanish, French, or Mandarin, to examine whether the observed biases are consistent across different linguistic groups. The current study only covers 21 states in the US, which is not sufficient to draw conclusions about the entire country. The authors should aim for a more balanced representation of participants from all 50 states. The small sample size of 135 participants is also a major limitation. The authors should increase the sample size to at least 500 participants to ensure that the results are statistically significant and generalizable.

In addition to expanding the participant pool, the authors should also refine their experimental design to include more control conditions. Specifically, they should conduct user studies on SDXL-Inc without revealing that the images are generated using SDXL-Inc, and compare the results with the "labeled as AI-generated" results. This will help to determine whether the labeling of the images as AI-generated influences the participants' perceptions of bias. The authors should also conduct user studies on other debiasing methods, such as ITI-GEN and Fair Diffusion, and compare the results with SDXL-Inc. This will help to determine whether the proposed method is more effective than existing debiasing techniques. The authors should also consider using a more diverse set of prompts to generate images, including prompts that are more complex and nuanced. This will help to ensure that the results are not biased towards a specific set of prompts. The authors should also consider using a more diverse set of attributes, including attributes that are not directly related to race and gender, such as age, socioeconomic status, and physical abilities.

Finally, the authors should provide a more detailed analysis of the results, including a breakdown of the results by demographic group. This will help to identify any potential biases in the results and to ensure that the conclusions are supported by the data. The authors should also consider using statistical methods to control for potential confounding variables, such as age, education level, and political affiliation. The authors should also provide a more detailed discussion of the limitations of their study and the potential implications of their findings. The authors should also consider the ethical implications of their work, including the potential for their work to be used to perpetuate biases and stereotypes. The authors should also consider the potential for their work to be used to create misleading or harmful content. The authors should also consider the potential for their work to be used to manipulate people's perceptions of reality.

### Questions

Please see the weaknesses.

### Rating

5

### Confidence

3

**********
