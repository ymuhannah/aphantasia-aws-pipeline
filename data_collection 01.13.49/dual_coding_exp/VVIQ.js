var VVIQ_survey = {
  type: jsPsychSurvey,
  css_classes: ['VVIQ_CSS'],
  show_question_numbers: "on",
  pages: [
    [
      {
        type: 'html',
        prompt: "<br><br><p style='text-align: centre;'><b>Vividness of Visual Imagery Questionnaire</b></p><br><p>For each item on this questionnaire, try to form a visual image, and consider your experience carefully. For any image that you do experience, rate how vivid it is using the five-point scale described below. If you do not have a visual image, rate vividness as '1'. Only use '5' for images that are truly as lively and vivid as real seeing. Please note that there are no right or wrong answers to the questions, and that it is not necessarily desirable to experience imagery or, if you do, to have more vivid imagery.</p><br><br><p>For items 1-4, think of some relative or friend whom you frequently see (but who is not with you at present) and consider carefully the picture that comes before your mind's eye.</p>",
      },
      {
        type: 'multi-choice',
        prompt: 'The exact contour of face, head, shoulders and body.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q1',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'Characteristic poses of head, attitudes of body etc.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q2',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'The precise carriage, length of step etc., in walking.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q3',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'The different colours worn in some familiar clothes.',
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q4',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'html',
        prompt: "<br><br><br><br><br><p>Visualise a rising sun. Consider carefully the picture that comes before your mind's eye.</p>",
      },
      {
        type: 'multi-choice',
        prompt: 'The sun rising above the horizon into a hazy sky.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q5',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'The sky clears and surrounds the sun with blueness.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q6',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'Clouds. A storm blows up with flashes of lightning.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q7',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'A rainbow appears.',
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q8',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'html',
        prompt: "<br><br><br><br><br><p>Think of the front of a shop which you often go to. Consider the picture that comes before your mind's eye.</p>",
      },
      {
        type: 'multi-choice',
        prompt: 'The overall appearance of the shop from the opposite side of the road.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q9',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'A window display including colours, shapes and details of individual items for sale.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q10',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'You are near the entrance. The colour, shape and details of the door.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q11',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'You enter the shop and go to the counter. The counter assistant serves you. Money changes hands.',
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q12',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'html',
        prompt: "<br><br><br><br><br><p>Finally, think of a country scene that involves trees, mountains, and a lake. Consider the picture that comes before your mind's eye.</p>",
      },
      {
        type: 'multi-choice',
        prompt: 'The contours of the landscape.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q13',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'The colour and shape of the trees.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q14',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'The colour and shape of the lake.', 
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q15',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'multi-choice',
        prompt: 'A strong wind blows on the trees and on the lake causing waves in the water.',
        options: ['1: No image at all, you only "know" that you are thinking of the object', '2: Vague and dim', '3: Moderately clear and lively', '4: Clear and reasonably vivid', '5: Perfectly clear and vivid as real seeing'],
        name: 'VVIQ_Q16',
        required: true,
        option_reorder: "none"
      },
      {
        type: 'html',
        prompt: "<br><br><br><br><br><p>When you are finished, click the button below.</p>",
      },
    ]
  ],
  on_finish: function(data) {
      // Collect VVIQ responses
      var vviqData = {};
      for (var i = 1; i <= 16; i++) {
          vviqData['VVIQ_Q' + i] = data.response['VVIQ_Q' + i];
      }
      jsPsych.data.addProperties(vviqData);
  }     
};