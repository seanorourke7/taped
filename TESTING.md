
Errors found on W3C validator that couldn't be fixed due to not being in my code/not accessible. 


From Product Management page:

Error: Duplicate attribute id.
At line 761, column 115
k rounded-0" id="id_image">↩</
Error: Element p not allowed as child of element strong in this context. (Suppressing further errors from this subtree.)
From line 763, column 9; to line 763, column 45
>↩<strong><p class="text-danger" id="filename"></p></


From the post detail view Errors attributed to the iFrame inserted automatically by django. 

Error: The frameborder attribute on the iframe element is obsolete. Use CSS instead.
From line 270, column 112; to line 270, column 273
br></p><p><iframe frameborder="0" src="https://instagram.com/p/C1csx9_IC5K/embed/" width="612" height="710" scrolling="no" allowtransparency="true" class="note-video-clip"></ifra
Error: The scrolling attribute on the iframe element is obsolete. Use CSS instead.
From line 270, column 112; to line 270, column 273
br></p><p><iframe frameborder="0" src="https://instagram.com/p/C1csx9_IC5K/embed/" width="612" height="710" scrolling="no" allowtransparency="true" class="note-video-clip"></ifra
Error: The allowtransparency attribute on the iframe element is obsolete. Use CSS instead.
From line 270, column 112; to line 270, column 273
br></p><p><iframe frameborder="0" src="https://instagram.com/p/C1csx9_IC5K/embed/" width="612" height="710" scrolling="no" allowtransparency="true" class="note-video-clip"></ifra
Error: No p element in scope but a p end tag seen.
From line 270, column 291; to line 270, column 294
e><br></p></p>↩     
Warning: The type attribute is unnecessary for JavaScript resources.
From line 366, column 5; to line 366, column 35
↩    ↩    <script type="text/javascript">↩   





From Edit Product page 
There is an error about the image not having an alt but it does have it in the initial loading on the product page.

Error: An img element must have an alt attribute, except under certain conditions. For details, consult guidance on providing text alternatives for images.
From line 785, column 9; to line 785, column 155
>↩        <img width="96" height="96" class="rounded shadow-sm" src="https://res.cloudinary.com/dwej6pult/image/upload/v1710087129/pdentylraw5mrozgsxsk.png">↩    <
Error: Duplicate attribute id.
At line 796, column 115
k rounded-0" id="id_image">↩</


Profile update page.

Error: Attribute placeholder not allowed on element select at this point.
From line 267, column 1821; to line 267, column 1966
p"> <div> <select name="default_county" placeholder="County *" class="border-black rounded-0 profile-form-input select form-control" id="id_default_county"> <opti
Attributes for element select:
Global attributes
autocomplete — Hint for form autofill feature
disabled — Whether the form control is disabled
form — Associates the element with a form element
multiple — Whether to allow multiple values
name — Name of the element to use for form submission and in the form.elements API
required — Whether the control is required for form submission
size — Size of the control