Backwards incompatible changes for the swaps application.

[r14](http://code.google.com/p/django-swaps/source/detail?r=14) If you were one of the few people using swaps from [django-social-economics](http://code.google.com/p/django-social-economics/), you will find here a database change.  The state fields in both Offer and Swap models have been changed from char to integer.