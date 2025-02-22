#ifndef COMMON_H
#define COMMON_H

#include <stdexcept>
#include <boost/version.hpp>

#ifdef _WIN32
    #define LIBLSL_CPP_API __declspec(dllexport)
#else
    #define LIBLSL_CPP_API
    #pragma GCC visibility push(default)
#endif


#if BOOST_VERSION < 104500
	#error "Please do not compile this with a boost version older than 1.45 because the library would otherwise not be protocol-compatible with builds using other versions."
#endif


// the highest supported protocol version
// * 100 is the original version, supported by library versions 1.00+
// * 110 is an alternative protocol that improves throughput, supported by library versions 1.10+
const int LSL_PROTOCOL_VERSION = 110;

// the library version
const int LSL_LIBRARY_VERSION = 110;

namespace lsl {
	/// A very large time duration (> 1 year) for timeout values.
	const double FOREVER = 32000000.0;

	/// Constant to indicate that a sample has the next successive time stamp.
	const double DEDUCED_TIMESTAMP = -1.0; 

	/// Constant to indicate that a stream has variable sampling rate.
	const double IRREGULAR_RATE = 0.0; 

	/// Obtain a local system time stamp in seconds.
	double lsl_clock();

	/// Data format of a channel (each transmitted sample holds an array of channels).
	enum channel_format_t {
		cf_float32 = 1,		// For up to 24-bit precision measurements in the appropriate physical unit 
							// (e.g., microvolts). Integers from -16777216 to 16777216 are represented accurately.
		cf_double64 = 2,	// For universal numeric data as long as permitted by network & disk budget. 
							// The largest representable integer is 53-bit.
		cf_string = 3,		// For variable-length ASCII strings or data blobs, such as video frames,
							// complex event descriptions, etc.
		cf_int32 = 4,		// For high-rate digitized formats that require 32-bit precision. Depends critically on 
							// meta-data to represent meaningful units. Useful for application event codes or other coded data.
		cf_int16 = 5,		// For very high rate signals (40Khz+) or consumer-grade audio
							// (for professional audio float is recommended).
		cf_int8 = 6,		// For binary signals or other coded data. 
							// Not recommended for encoding string data.
		cf_int64 = 7,		// For now only for future compatibility. Support for this type is not yet exposed in all languages. 
							// Also, some builds of liblsl will not be able to send or receive data of this type.
		cf_undefined = 0	// Can not be transmitted.
	};

	/// Exception class that indicates that a stream inlet's source has been irrecoverably lost.
	class LIBLSL_CPP_API lost_error: public std::runtime_error {
	public:
		explicit lost_error(const std::string &msg): std::runtime_error(msg) {}
	};


	/// Exception class that indicates that an operation failed due to a timeout.
	class LIBLSL_CPP_API timeout_error: public std::runtime_error {
	public:
		explicit timeout_error(const std::string &msg): std::runtime_error(msg) {}
	};
}

#ifndef _WIN32
#pragma GCC visibility pop
#endif


// === Auto-generated target platform version defines (for Microsoft and asio) ===

#ifndef WINVER
#define WINVER 0x0501
#endif

#ifndef _WIN32_WINNT
#define _WIN32_WINNT 0x0501
#endif

#ifndef _WIN32_WINDOWS
#define _WIN32_WINDOWS 0x0501
#endif

#ifndef _WIN32_IE
#define _WIN32_IE 0x0500
#endif


#endif

