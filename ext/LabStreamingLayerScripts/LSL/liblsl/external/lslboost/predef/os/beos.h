/*
Copyright Redshift Software, Inc. 2008-2013
Distributed under the Boost Software License, Version 1.0.
(See accompanying file LICENSE_1_0.txt or copy at
http://www.lslboost.org/LICENSE_1_0.txt)
*/

#ifndef BOOST_PREDEF_OS_BEOS_H
#define BOOST_PREDEF_OS_BEOS_H

#include <lslboost/predef/version_number.h>
#include <lslboost/predef/make.h>

/*`
[heading `BOOST_OS_BEOS`]

[@http://en.wikipedia.org/wiki/BeOS BeOS] operating system.

[table
    [[__predef_symbol__] [__predef_version__]]

    [[`__BEOS__`] [__predef_detection__]]
    ]
 */

#define BOOST_OS_BEOS BOOST_VERSION_NUMBER_NOT_AVAILABLE

#if !BOOST_PREDEF_DETAIL_OS_DETECTED && ( \
    defined(__BEOS__) \
    )
#   undef BOOST_OS_BEOS
#   define BOOST_OS_BEOS BOOST_VERSION_NUMBER_AVAILABLE
#endif

#if BOOST_OS_BEOS
#   define BOOST_OS_BEOS_AVAILABLE
#   include <lslboost/predef/detail/os_detected.h>
#endif

#define BOOST_OS_BEOS_NAME "BeOS"

#include <lslboost/predef/detail/test.h>
BOOST_PREDEF_DECLARE_TEST(BOOST_OS_BEOS,BOOST_OS_BEOS_NAME)


#endif
