《Learn Objective-C On the Mac》Note
=================================
《Objective-C 基础教程》笔记
---------------------------------
###1. Hello###

###2. Extensions to C###
  \#import 


  NSLog
  
  
  %@
  
  
  @"string"
  
  
  BOOL YES NO

###3. OOP###

	self

<pre>	
/* class.h BEGIN */
@interface Class:NSObject
{
	int _member;
}	

- (int)function:(int)parameter;

- (void)many_parameters_function:(int)parameter1 some_information:(NString *)parameter2;

- (void)no_parameter_function;
@end //Class
/* class.h END */
</pre>
<pre>
/* class.m BEGIN */
@implementation Class
- (int)function:(int)p 
{
}//function
- (void)many_parameters_function:(int)p1 some_information:(NString *)p2
{
}//many_parameters_function
- (void)no_parameter_function
{
} //noparameter_function
@end //Class
/* class.m END */
	</pre>

###4. Inheritance###
	
Objective-C does not support multiple inheritance

<pre>
 /* Children.h BEGIN */
@interface Children : Parent
 
@end //Children
/* Children.h END */
</pre>

super

isa()
	
overridden


###5. Composition###
  description

###6. Organization###
  @class sets up a forward reference


###7. More About Xcode###

defaults write com.apple.Xcode PBXCustomTemplateMacroDefinitions



'{"ORGANIZATIONNAME" = "zuohaitao";}'


command+shift+E


File->Make Snapshot


File->Snapshots


command+D


Help->Show Research Assistant.



##8. Foundation Kit##

<pre>
  NSRange
    typedef struct _NSRange NSRange;
    struct _NSRange
    {
        NSUInteger location;
        NSUInteger length;
    };
</pre>
<pre>
  NSPoint
    typedef struct _NSPoint NSPoint;
    struct _NSPoint
    {
        CGFloat x;
        CGFloat y;
    };
</pre>
<pre>
  NSSize
    typedef struct _NSSize NSSize;
    struct _NSSize
    {
        CGFloat width;
        CGFloat height;
    };
</pre>
<pre>
  NSRect
    typedef struct _NSRect NSRect;
    struct _NSRect
    {
        NSPoint origin;
        NSSize size;
    };
</pre>
<pre>
  NSString
    + (id)stringWithFormat:(NSString *)format,...
    - (unsigned int)length
    - (BOOL)isEqualToString:(NSString *)aString
    - (NSComparisonResult)compare:(NSString *) string;
    - (NSComparisonResult)compare:(NSString *) string 
                          options:(unsigned) mask;
    - (BOOL)hasPrefix:(NSString *)aString;
    - (BOOL)hasSuffix:(NSString *)aString;
    - (NSRange)rangeOfString:(NSString *) aString;
    - (NSArray *)componentsSeparatedByString:(NSString *)separator
    - (NSString *)componentsJoinedByString:(NSString *)separator
    - (NSString *)stringByExpandingTildeInPath
</pre>
<pre>
  NSMutableString
    + (id)stringWithCapacity:(unsigned)capacity;
    - (void)appendString:(NSString *)aString;
    - (void)appendFormat:(NSString *)format, ...;
    - (void)deleteCharactersInRange:(NSRange)range;
</pre>
<pre>
  NSArray
    + (id)arrayWithObjects:(id)firstObj,...;
    - (unsigned)count;
    - (id)objectAtIndex:(unsigned int) index;
</pre>
<pre>
  NSMutableArray
    + (id)arrayWithCapacity:(unsigned) numItems;
    - (void)addObject:(id)anObject;
    - (void)removeObjectAtIndex:(unsigned)index;
    - (NSEnumerator *)objectEnumerator;
    - (id)nextObject;
</pre>
<pre>
        /* enumeration */
        NSEnumerator *enumerator;
        enumerator = [array objectEnumerator];
        id thingie;
        while(thingie = [enumerator nextObject]) {
            NSLog(@"I found %@", thingie);
        }
        /* Fast Enumeration */
        for(NSString *string in array) {
            NSLog(@"I found %@", string);
        }
</pre>
<pre>
  NSDictionary
    + (id)dictionaryWithObjectsAndKeys:(id)firstObject, (id)firstKey, ...;
    - (id)objectForKey:(id)aKey;
</pre>
<pre>
  NSMutableDictionary
    + (id)dictionaryWithCapacity:(unsigned int)numItems;
    - (void)setObject:(id)anObject forKey:(id)aKey;
    - (void)removeObjectForKey:(id)aKey;
</pre>


because in Cocoa may classes are implemented as class clusters,


don't create subclass to extend, use categories. 


<pre>
  NSNumber
    + (NSNumber *)numberWithChar:(char)value;
    + (NSNumber *)numberWithInt:(int)value;
    + (NSNumber *)numberWithFloat:(float)value;
    + (NSNumber *)numberWithBool:(BOOL)value;
    - (char)charValue;
    - (int)intValue;
    - (float)floatValue;
    - (BOOL)boolValue;
    - (NSString *)stringValue;
</pre>
<pre>
  NSValue
    + (NSValue *)valueWithBytes:(const void *)value
                       objCType:(const char *)type;
    + (NSValue *)valueWithPoint:(NSPoint)point;
    + (NSValue *)valueWithSize:(NSSize)size;
    + (NSValue *)valueWithRect:(NSRect)rect;
    - (NSPoint)pointValue;
    - (NSSize)sizeValue;
    - (NSRect)rectValue;
</pre>
<pre>
  NSNull
    + (NSNull *) null;
</pre>
<pre>
  NSFileManager
    + (NSFileManager *)defaultManager
    - (NSDirectoryEnumerator *)enumeratorAtPath:(NSString *)path
</pre>

###9.0 Memory Management###

+ Garbage Collection(GC)
	
If you know that your programs will only be run on Leopard or later, 
you can take advantage of Objective-C 2.0's garbage collection

+ Reference Counting(RC)

Automatic Reference Counting(ARC)



ARC is supported in Xcode 4.2 for OS X v10.6 and v10.7 (64-bit applications) and for iOS 4 and iOS 5. 
		
		
Weak references are not supported in OS X v10.6 and iOS 4.

+ Manual Reference Counting(MRC)

		- (id)retain;
		-(oneway void)release;

oneway is used with the distributed objects API, 
which allows use of objective\-c objects between 
different threads or applications. It tells the 
system that it should not block the calling thread 
until the method returns. Without it, the caller 
will block, even though the method's return type 
is void. Obviously, it is never used with anything 
other than void, as doing so would mean the method 
returns something, but the caller doesn't get it.

        - (unsigned)retainCount;
        - (id)autorelease;

  The Rules of Cocoa Memory Management                                                     

<pre>
   +----------------+-------------------------+--------------------------------------------+
   |Obtained Via... |Transient                |Hang On                                     |
   +----------------+-------------------------+--------------------------------------------+
   |alloc/new/copy  |Release when done        | Release in dealloc                         |
   +----------------+-------------------------+--------------------------------------------+
   |Any other way   |Don't need to do anything| Retain when acquired, release in dealloc   |
   +----------------+-------------------------+--------------------------------------------+
</pre>


        /* Keeping The Pool Clean */
        NSAutoreleasePool *pool;
        pool = [[NSAutoreleasePool alloc] init];
        int i;
        for (i = 0; i < 1000000; i++) {
            id object = [someArray objectAtIndex: i];
            NSString *desc = [object descrption];
            // and do something with the description
            if (i % 1000 == 0) {
            [pool release];
            pool = [[NSAutoreleasePool alloc] init];
            }
        }
        [pool release]
        /* Keeping The Pool Clean */
###10. Object Initialization###
###11. Properties###


Objective-C 2.0 features can only be used on Mac OS X 10.5 (Leopard) or later


@property


assign retain copy


readonly readwrite


nonatomic


@synthesize

###12.Categories###
<pre>
		@interface ClassName(CategoryName)

		@end //interface ClassName(CategoryName)
</pre>	
<pre>
		@implementation ClassName(CategoryName)

		@end //implementation ClassName(CategoryName)
</pre>

+ Bad Category

	1. You can not add variables to class.

	2. When names collide, the category wins.
  
+ Purpose

	1. split class implementation into multiple files or multiple frameworks
		
	2. creating forward references for private methods
		
	3. adding informal protocols to an object

+ Delegate
    

delegate is an object asked by another object to do some of its work.
    
	
e.g. the AppKit class NSApplication asks its delegate if it should open an Untitled window when the application launches.


@selector(func:)

	
[obj respondsToSelector:@selector(func:)]


###13. Protocols###
<pre>
	@protocol FormalProtocolA
    
	- (void)functionA;
    
	@end //protocol FormalProtocolA
</pre>
<pre>
	@protocol FormalProtocolB
    - (void)functionB;
    @end //protocol FormalProtocolB
</pre>
<pre>
    @interface Obj:NSObject
    @end //interface Obj
</pre>
<pre>
    @implementation Obj
    - (void)functionA
    {
    }
    - (void)functionB
    {
    }
    @end //interface Obj
</pre>
+ A shallow copy

	you don't duplicate the referred objects; 
    
	
	you new copy simply points at the referred objects that already exist.


+ A deep copy

	makes duplicates of all the referred objects.
<pre>
    - (id)copyWithZone:(NSZone *)zone
    {
        return [[[self class] allocWithZone: zone]init];
    }
</pre>
    

+ Objective\-C 2.0
    
+ @optional
    	
+ @required

   


